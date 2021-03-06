[@@@ocaml.warning "-27-30-39"]

type terminal_constraint_mutable = {
  mutable category : string;
  mutable start : int;
}

let default_terminal_constraint_mutable () : terminal_constraint_mutable = {
  category = "";
  start = 0;
}

type non_terminal_constraint_mutable = {
  mutable category : string option;
  mutable start : int;
  mutable length : int;
}

let default_non_terminal_constraint_mutable () : non_terminal_constraint_mutable = {
  category = None;
  start = 0;
  length = 0;
}

type attribute_mutable = {
  mutable lemma : string option;
  mutable pos : string option;
  mutable chunk : string option;
  mutable entity : string option;
}

let default_attribute_mutable () : attribute_mutable = {
  lemma = None;
  pos = None;
  chunk = None;
  entity = None;
}

type matrix_mutable = {
  mutable values : float list;
  mutable shape : int list;
}

let default_matrix_mutable () : matrix_mutable = {
  values = [];
  shape = [];
}

type ccgseed_mutable = {
  mutable id : string option;
  mutable sentence : string list;
  mutable cat_probs : Ccg_seed_types.matrix;
  mutable dep_probs : Ccg_seed_types.matrix;
  mutable attribs : Ccg_seed_types.attribute list;
  mutable constraints : Ccg_seed_types.constraint_ list;
}

let default_ccgseed_mutable () : ccgseed_mutable = {
  id = None;
  sentence = [];
  cat_probs = Ccg_seed_types.default_matrix ();
  dep_probs = Ccg_seed_types.default_matrix ();
  attribs = [];
  constraints = [];
}

type ccgseeds_mutable = {
  mutable lang : string;
  mutable categories : string list;
  mutable seeds : Ccg_seed_types.ccgseed list;
}

let default_ccgseeds_mutable () : ccgseeds_mutable = {
  lang = "";
  categories = [];
  seeds = [];
}


let rec decode_terminal_constraint d =
  let v = default_terminal_constraint_mutable () in
  let continue__= ref true in
  let start_is_set = ref false in
  let category_is_set = ref false in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
    ); continue__ := false
    | Some (1, Pbrt.Bytes) -> begin
      v.category <- Pbrt.Decoder.string d; category_is_set := true;
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(terminal_constraint), field(1)" pk
    | Some (2, Pbrt.Varint) -> begin
      v.start <- Pbrt.Decoder.int_as_varint d; start_is_set := true;
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(terminal_constraint), field(2)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  begin if not !start_is_set then Pbrt.Decoder.missing_field "start" end;
  begin if not !category_is_set then Pbrt.Decoder.missing_field "category" end;
  ({
    Ccg_seed_types.category = v.category;
    Ccg_seed_types.start = v.start;
  } : Ccg_seed_types.terminal_constraint)

let rec decode_non_terminal_constraint d =
  let v = default_non_terminal_constraint_mutable () in
  let continue__= ref true in
  let length_is_set = ref false in
  let start_is_set = ref false in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
    ); continue__ := false
    | Some (1, Pbrt.Bytes) -> begin
      v.category <- Some (Pbrt.Decoder.string d);
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(non_terminal_constraint), field(1)" pk
    | Some (2, Pbrt.Varint) -> begin
      v.start <- Pbrt.Decoder.int_as_varint d; start_is_set := true;
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(non_terminal_constraint), field(2)" pk
    | Some (3, Pbrt.Varint) -> begin
      v.length <- Pbrt.Decoder.int_as_varint d; length_is_set := true;
    end
    | Some (3, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(non_terminal_constraint), field(3)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  begin if not !length_is_set then Pbrt.Decoder.missing_field "length" end;
  begin if not !start_is_set then Pbrt.Decoder.missing_field "start" end;
  ({
    Ccg_seed_types.category = v.category;
    Ccg_seed_types.start = v.start;
    Ccg_seed_types.length = v.length;
  } : Ccg_seed_types.non_terminal_constraint)

let rec decode_constraint_ d = 
  let rec loop () = 
    let ret:Ccg_seed_types.constraint_ = match Pbrt.Decoder.key d with
      | None -> Pbrt.Decoder.malformed_variant "constraint_"
      | Some (1, _) -> Ccg_seed_types.Terminal (decode_terminal_constraint (Pbrt.Decoder.nested d))
      | Some (2, _) -> Ccg_seed_types.Nonterminal (decode_non_terminal_constraint (Pbrt.Decoder.nested d))
      | Some (n, payload_kind) -> (
        Pbrt.Decoder.skip d payload_kind; 
        loop () 
      )
    in
    ret
  in
  loop ()

let rec decode_attribute d =
  let v = default_attribute_mutable () in
  let continue__= ref true in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
    ); continue__ := false
    | Some (1, Pbrt.Bytes) -> begin
      v.lemma <- Some (Pbrt.Decoder.string d);
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(attribute), field(1)" pk
    | Some (2, Pbrt.Bytes) -> begin
      v.pos <- Some (Pbrt.Decoder.string d);
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(attribute), field(2)" pk
    | Some (3, Pbrt.Bytes) -> begin
      v.chunk <- Some (Pbrt.Decoder.string d);
    end
    | Some (3, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(attribute), field(3)" pk
    | Some (4, Pbrt.Bytes) -> begin
      v.entity <- Some (Pbrt.Decoder.string d);
    end
    | Some (4, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(attribute), field(4)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  ({
    Ccg_seed_types.lemma = v.lemma;
    Ccg_seed_types.pos = v.pos;
    Ccg_seed_types.chunk = v.chunk;
    Ccg_seed_types.entity = v.entity;
  } : Ccg_seed_types.attribute)

let rec decode_matrix d =
  let v = default_matrix_mutable () in
  let continue__= ref true in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
      v.shape <- List.rev v.shape;
      v.values <- List.rev v.values;
    ); continue__ := false
    | Some (1, Pbrt.Bits64) -> begin
      v.values <- (Pbrt.Decoder.float_as_bits64 d) :: v.values;
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(matrix), field(1)" pk
    | Some (2, Pbrt.Varint) -> begin
      v.shape <- (Pbrt.Decoder.int_as_varint d) :: v.shape;
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(matrix), field(2)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  ({
    Ccg_seed_types.values = v.values;
    Ccg_seed_types.shape = v.shape;
  } : Ccg_seed_types.matrix)

let rec decode_ccgseed d =
  let v = default_ccgseed_mutable () in
  let continue__= ref true in
  let dep_probs_is_set = ref false in
  let cat_probs_is_set = ref false in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
      v.constraints <- List.rev v.constraints;
      v.attribs <- List.rev v.attribs;
      v.sentence <- List.rev v.sentence;
    ); continue__ := false
    | Some (1, Pbrt.Bytes) -> begin
      v.id <- Some (Pbrt.Decoder.string d);
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(1)" pk
    | Some (2, Pbrt.Bytes) -> begin
      v.sentence <- (Pbrt.Decoder.string d) :: v.sentence;
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(2)" pk
    | Some (3, Pbrt.Bytes) -> begin
      v.cat_probs <- decode_matrix (Pbrt.Decoder.nested d); cat_probs_is_set := true;
    end
    | Some (3, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(3)" pk
    | Some (4, Pbrt.Bytes) -> begin
      v.dep_probs <- decode_matrix (Pbrt.Decoder.nested d); dep_probs_is_set := true;
    end
    | Some (4, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(4)" pk
    | Some (5, Pbrt.Bytes) -> begin
      v.attribs <- (decode_attribute (Pbrt.Decoder.nested d)) :: v.attribs;
    end
    | Some (5, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(5)" pk
    | Some (6, Pbrt.Bytes) -> begin
      v.constraints <- (decode_constraint_ (Pbrt.Decoder.nested d)) :: v.constraints;
    end
    | Some (6, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseed), field(6)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  begin if not !dep_probs_is_set then Pbrt.Decoder.missing_field "dep_probs" end;
  begin if not !cat_probs_is_set then Pbrt.Decoder.missing_field "cat_probs" end;
  ({
    Ccg_seed_types.id = v.id;
    Ccg_seed_types.sentence = v.sentence;
    Ccg_seed_types.cat_probs = v.cat_probs;
    Ccg_seed_types.dep_probs = v.dep_probs;
    Ccg_seed_types.attribs = v.attribs;
    Ccg_seed_types.constraints = v.constraints;
  } : Ccg_seed_types.ccgseed)

let rec decode_ccgseeds d =
  let v = default_ccgseeds_mutable () in
  let continue__= ref true in
  let lang_is_set = ref false in
  while !continue__ do
    match Pbrt.Decoder.key d with
    | None -> (
      v.seeds <- List.rev v.seeds;
      v.categories <- List.rev v.categories;
    ); continue__ := false
    | Some (1, Pbrt.Bytes) -> begin
      v.lang <- Pbrt.Decoder.string d; lang_is_set := true;
    end
    | Some (1, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseeds), field(1)" pk
    | Some (2, Pbrt.Bytes) -> begin
      v.categories <- (Pbrt.Decoder.string d) :: v.categories;
    end
    | Some (2, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseeds), field(2)" pk
    | Some (3, Pbrt.Bytes) -> begin
      v.seeds <- (decode_ccgseed (Pbrt.Decoder.nested d)) :: v.seeds;
    end
    | Some (3, pk) -> 
      Pbrt.Decoder.unexpected_payload "Message(ccgseeds), field(3)" pk
    | Some (_, payload_kind) -> Pbrt.Decoder.skip d payload_kind
  done;
  begin if not !lang_is_set then Pbrt.Decoder.missing_field "lang" end;
  ({
    Ccg_seed_types.lang = v.lang;
    Ccg_seed_types.categories = v.categories;
    Ccg_seed_types.seeds = v.seeds;
  } : Ccg_seed_types.ccgseeds)

let rec encode_terminal_constraint (v:Ccg_seed_types.terminal_constraint) encoder = 
  Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
  Pbrt.Encoder.string v.Ccg_seed_types.category encoder;
  Pbrt.Encoder.key (2, Pbrt.Varint) encoder; 
  Pbrt.Encoder.int_as_varint v.Ccg_seed_types.start encoder;
  ()

let rec encode_non_terminal_constraint (v:Ccg_seed_types.non_terminal_constraint) encoder = 
  begin match v.Ccg_seed_types.category with
  | Some x -> 
    Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  Pbrt.Encoder.key (2, Pbrt.Varint) encoder; 
  Pbrt.Encoder.int_as_varint v.Ccg_seed_types.start encoder;
  Pbrt.Encoder.key (3, Pbrt.Varint) encoder; 
  Pbrt.Encoder.int_as_varint v.Ccg_seed_types.length encoder;
  ()

let rec encode_constraint_ (v:Ccg_seed_types.constraint_) encoder = 
  begin match v with
  | Ccg_seed_types.Terminal x ->
    Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.nested (encode_terminal_constraint x) encoder;
  | Ccg_seed_types.Nonterminal x ->
    Pbrt.Encoder.key (2, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.nested (encode_non_terminal_constraint x) encoder;
  end

let rec encode_attribute (v:Ccg_seed_types.attribute) encoder = 
  begin match v.Ccg_seed_types.lemma with
  | Some x -> 
    Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  begin match v.Ccg_seed_types.pos with
  | Some x -> 
    Pbrt.Encoder.key (2, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  begin match v.Ccg_seed_types.chunk with
  | Some x -> 
    Pbrt.Encoder.key (3, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  begin match v.Ccg_seed_types.entity with
  | Some x -> 
    Pbrt.Encoder.key (4, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  ()

let rec encode_matrix (v:Ccg_seed_types.matrix) encoder = 
  List.iter (fun x -> 
    Pbrt.Encoder.key (1, Pbrt.Bits64) encoder; 
    Pbrt.Encoder.float_as_bits64 x encoder;
  ) v.Ccg_seed_types.values;
  List.iter (fun x -> 
    Pbrt.Encoder.key (2, Pbrt.Varint) encoder; 
    Pbrt.Encoder.int_as_varint x encoder;
  ) v.Ccg_seed_types.shape;
  ()

let rec encode_ccgseed (v:Ccg_seed_types.ccgseed) encoder = 
  begin match v.Ccg_seed_types.id with
  | Some x -> 
    Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  | None -> ();
  end;
  List.iter (fun x -> 
    Pbrt.Encoder.key (2, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  ) v.Ccg_seed_types.sentence;
  Pbrt.Encoder.key (3, Pbrt.Bytes) encoder; 
  Pbrt.Encoder.nested (encode_matrix v.Ccg_seed_types.cat_probs) encoder;
  Pbrt.Encoder.key (4, Pbrt.Bytes) encoder; 
  Pbrt.Encoder.nested (encode_matrix v.Ccg_seed_types.dep_probs) encoder;
  List.iter (fun x -> 
    Pbrt.Encoder.key (5, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.nested (encode_attribute x) encoder;
  ) v.Ccg_seed_types.attribs;
  List.iter (fun x -> 
    Pbrt.Encoder.key (6, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.nested (encode_constraint_ x) encoder;
  ) v.Ccg_seed_types.constraints;
  ()

let rec encode_ccgseeds (v:Ccg_seed_types.ccgseeds) encoder = 
  Pbrt.Encoder.key (1, Pbrt.Bytes) encoder; 
  Pbrt.Encoder.string v.Ccg_seed_types.lang encoder;
  List.iter (fun x -> 
    Pbrt.Encoder.key (2, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.string x encoder;
  ) v.Ccg_seed_types.categories;
  List.iter (fun x -> 
    Pbrt.Encoder.key (3, Pbrt.Bytes) encoder; 
    Pbrt.Encoder.nested (encode_ccgseed x) encoder;
  ) v.Ccg_seed_types.seeds;
  ()
