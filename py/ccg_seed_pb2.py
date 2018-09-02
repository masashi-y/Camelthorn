# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ccg_seed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ccg_seed.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x63\x63g_seed.proto\"=\n\nConstraint\x12\x10\n\x08\x63\x61tegory\x18\x01 \x02(\t\x12\r\n\x05start\x18\x02 \x02(\x05\x12\x0e\n\x06length\x18\x03 \x02(\x05\"F\n\tAttribute\x12\r\n\x05lemma\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\t\x12\r\n\x05\x63hunk\x18\x03 \x01(\t\x12\x0e\n\x06\x65ntity\x18\x04 \x01(\t\"E\n\x08\x43\x43GSeeds\x12\x0c\n\x04lang\x18\x01 \x02(\t\x12\x12\n\ncategories\x18\x02 \x03(\t\x12\x17\n\x05seeds\x18\x03 \x03(\x0b\x32\x08.CCGSeed\"\x9e\x01\n\x07\x43\x43GSeed\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08sentence\x18\x02 \x03(\t\x12\x1a\n\tcat_probs\x18\x03 \x02(\x0b\x32\x07.Matrix\x12\x1a\n\tdep_probs\x18\x04 \x02(\x0b\x32\x07.Matrix\x12\x1b\n\x07\x61ttribs\x18\x05 \x03(\x0b\x32\n.Attribute\x12 \n\x0b\x63onstraints\x18\x06 \x03(\x0b\x32\x0b.Constraint\"/\n\x06Matrix\x12\x12\n\x06values\x18\x01 \x03(\x01\x42\x02\x10\x00\x12\x11\n\x05shape\x18\x02 \x03(\x05\x42\x02\x10\x00')
)




_CONSTRAINT = _descriptor.Descriptor(
  name='Constraint',
  full_name='Constraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='Constraint.category', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='Constraint.start', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='Constraint.length', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=79,
)


_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lemma', full_name='Attribute.lemma', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='Attribute.pos', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='Attribute.chunk', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity', full_name='Attribute.entity', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=151,
)


_CCGSEEDS = _descriptor.Descriptor(
  name='CCGSeeds',
  full_name='CCGSeeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lang', full_name='CCGSeeds.lang', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categories', full_name='CCGSeeds.categories', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seeds', full_name='CCGSeeds.seeds', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=222,
)


_CCGSEED = _descriptor.Descriptor(
  name='CCGSeed',
  full_name='CCGSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CCGSeed.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sentence', full_name='CCGSeed.sentence', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cat_probs', full_name='CCGSeed.cat_probs', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dep_probs', full_name='CCGSeed.dep_probs', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribs', full_name='CCGSeed.attribs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='CCGSeed.constraints', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=383,
)


_MATRIX = _descriptor.Descriptor(
  name='Matrix',
  full_name='Matrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='Matrix.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='Matrix.shape', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\000'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=432,
)

_CCGSEEDS.fields_by_name['seeds'].message_type = _CCGSEED
_CCGSEED.fields_by_name['cat_probs'].message_type = _MATRIX
_CCGSEED.fields_by_name['dep_probs'].message_type = _MATRIX
_CCGSEED.fields_by_name['attribs'].message_type = _ATTRIBUTE
_CCGSEED.fields_by_name['constraints'].message_type = _CONSTRAINT
DESCRIPTOR.message_types_by_name['Constraint'] = _CONSTRAINT
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['CCGSeeds'] = _CCGSEEDS
DESCRIPTOR.message_types_by_name['CCGSeed'] = _CCGSEED
DESCRIPTOR.message_types_by_name['Matrix'] = _MATRIX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Constraint = _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINT,
  __module__ = 'ccg_seed_pb2'
  # @@protoc_insertion_point(class_scope:Constraint)
  ))
_sym_db.RegisterMessage(Constraint)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTE,
  __module__ = 'ccg_seed_pb2'
  # @@protoc_insertion_point(class_scope:Attribute)
  ))
_sym_db.RegisterMessage(Attribute)

CCGSeeds = _reflection.GeneratedProtocolMessageType('CCGSeeds', (_message.Message,), dict(
  DESCRIPTOR = _CCGSEEDS,
  __module__ = 'ccg_seed_pb2'
  # @@protoc_insertion_point(class_scope:CCGSeeds)
  ))
_sym_db.RegisterMessage(CCGSeeds)

CCGSeed = _reflection.GeneratedProtocolMessageType('CCGSeed', (_message.Message,), dict(
  DESCRIPTOR = _CCGSEED,
  __module__ = 'ccg_seed_pb2'
  # @@protoc_insertion_point(class_scope:CCGSeed)
  ))
_sym_db.RegisterMessage(CCGSeed)

Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), dict(
  DESCRIPTOR = _MATRIX,
  __module__ = 'ccg_seed_pb2'
  # @@protoc_insertion_point(class_scope:Matrix)
  ))
_sym_db.RegisterMessage(Matrix)


_MATRIX.fields_by_name['values']._options = None
_MATRIX.fields_by_name['shape']._options = None
# @@protoc_insertion_point(module_scope)
