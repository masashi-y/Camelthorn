
from __future__ import print_function
import sys
import os
import numpy as np
import json
import chainer
import chainer.links as L
import chainer.functions as F
from chainer import cuda
from chainer import training, Variable
from chainer.training import extensions
from chainer.optimizer import WeightDecay, GradientClipping
from collections import defaultdict, OrderedDict

from py_utils import read_pretrained_embeddings, read_model_defs
from biaffine import Biaffine
from param import Param

UNK = "*UNKNOWN*"
START = "*START*"
END = "*END*"
IGNORE = -1

class FeatureExtractor(object):
    def __init__(self, model_path):
        self.model_path = model_path
        self.words = read_model_defs(model_path / 'words.txt')
        self.chars = read_model_defs(model_path / 'chars.txt')
        self.unk_word = self.words[UNK]
        self.start_word = self.words[START]
        self.end_word = self.words[END]
        self.unk_char = self.chars[UNK]
        self.start_char = self.chars[START]
        self.end_char = self.chars[END]

    def process(self, words):
        """
        words: list of unicode tokens
        """
        w = np.array([self.start_word] + [self.words.get(
            x, self.unk_word) for x in words] + [self.end_word], 'i')
        l = max(len(x) for x in words)
        c = -np.ones((len(words) + 2, l), 'i')
        c[0, 0] = self.start_char
        c[-1, 0] = self.end_char
        for i, word in enumerate(words, 1):
            for j in range(len(word)):
                c[i, j] = self.chars.get(word[j], self.unk_char)
        return w, c, np.array([l], 'i')



class BiaffineJaLSTMParser(chainer.Chain):
    def __init__(self, model_path):
        Param.load(self, model_path / 'tagger_defs.txt')
        self.extractor = FeatureExtractor(model_path)
        self.in_dim = self.word_dim + self.char_dim
        self.dropout_ratio = dropout_ratio
        super(BiaffineJaLSTMParser, self).__init__(
                emb_word=L.EmbedID(self.n_words, self.word_dim),
                emb_char=L.EmbedID(self.n_chars, 50, ignore_label=IGNORE),
                conv_char=L.Convolution2D(1, self.char_dim,
                    (3, 50), stride=1, pad=(1, 0)),
                lstm_f=L.NStepLSTM(self.nlayers, self.in_dim,
                    self.hidden_dim, 0.32),
                lstm_b=L.NStepLSTM(self.nlayers, self.in_dim,
                    self.hidden_dim, 0.32),
                arc_dep=L.Linear(2 * self.hidden_dim, self.dep_dim),
                arc_head=L.Linear(2 * self.hidden_dim, self.dep_dim),
                rel_dep=L.Linear(2 * self.hidden_dim, self.dep_dim),
                rel_head=L.Linear(2 * self.hidden_dim, self.dep_dim),
                biaffine_arc=Biaffine(self.dep_dim),
                biaffine_tag=L.Bilinear(self.dep_dim, self.dep_dim, len(self.targets)))

    def forward(self, ws, cs, ls, dep_ts=None):
        batchsize = len(ws)
        xp = chainer.cuda.get_array_module(ws[0])
        ws = map(self.emb_word, ws)
        cs = [F.squeeze(
            F.max_pooling_2d(
                self.conv_char(
                    F.expand_dims(
                        self.emb_char(c), 1)), (int(l[0]), 1)))
                    for c, l in zip(cs, ls)]
        xs_f = [F.dropout(F.concat([w, c]),
            self.dropout_ratio) for w, c in zip(ws, cs)]
        xs_b = [x[::-1] for x in xs_f]
        cx_f, hx_f, cx_b, hx_b = self._init_state(xp, batchsize)
        _, _, hs_f = self.lstm_f(hx_f, cx_f, xs_f)
        _, _, hs_b = self.lstm_b(hx_b, cx_b, xs_b)
        hs_b = [x[::-1] for x in hs_b]
        hs = [F.concat([h_f, h_b]) for h_f, h_b in zip(hs_f, hs_b)]

        dep_ys = [self.biaffine_arc(
            F.elu(F.dropout(self.arc_dep(h), 0.32)),
            F.elu(F.dropout(self.arc_head(h), 0.32))) for h in hs]

        if dep_ts is not None:
            heads = dep_ts
        else:
            heads = [F.argmax(y, axis=1) for y in dep_ys]

        cat_ys = [
                self.biaffine_tag(
            F.elu(F.dropout(self.rel_dep(h), 0.32)),
            F.elu(F.dropout(self.rel_head(
                F.embed_id(t, h, ignore_label=IGNORE)), 0.32))) \
                        for h, t in zip(hs, heads)]

        return cat_ys, dep_ys

    def predict(self, xs):
        xs = [self.extractor.process(x) for x in xs]
        ws, ss, ps = zip(*xs)
        with chainer.no_backprop_mode(), chainer.using_config('train', False):
            cat_ys, dep_ys = self.forward(ws, ss, ps)
        return zip([F.log_softmax(y[1:-1]).data for y in cat_ys],
                [F.log_softmax(y[1:-1, :-1]).data for y in dep_ys])

    def predict_doc(self, doc, batchsize=16):
        res = []
        for i in range(0, len(doc), batchsize):
            res.extend([(i + j, 0, y)
                for j, y in enumerate(self.predict(doc[i:i + batchsize]))])
        return res

    def _init_state(self, xp, batchsize):
        res = [Variable(xp.zeros(( # forward cx, hx, backward cx, hx
                self.nlayers, batchsize, self.hidden_dim), 'f')) for _ in range(4)]
        return res

    @property
    def cats(self):
        return list(zip(*sorted(self.targets.items(), key=lambda x: x[1])))[0]


