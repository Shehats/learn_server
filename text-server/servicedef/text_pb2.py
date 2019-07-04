# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='text.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntext.proto\",\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\"*\n\x08Releated\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x10\n\x08relation\x18\x02 \x01(\x02\"/\n\x0cTextResponse\x12\x1f\n\x0crelatedWords\x18\x01 \x03(\x0b\x32\t.Releated2C\n\x0bTextService\x12\x34\n\x0fGetRelatedWords\x12\x0c.TextRequest\x1a\r.TextResponse\"\x00(\x01\x30\x01\x62\x06proto3')
)




_TEXTREQUEST = _descriptor.Descriptor(
  name='TextRequest',
  full_name='TextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='TextRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='TextRequest.context', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=58,
)


_RELEATED = _descriptor.Descriptor(
  name='Releated',
  full_name='Releated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='Releated.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Releated.relation', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=102,
)


_TEXTRESPONSE = _descriptor.Descriptor(
  name='TextResponse',
  full_name='TextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relatedWords', full_name='TextResponse.relatedWords', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=151,
)

_TEXTRESPONSE.fields_by_name['relatedWords'].message_type = _RELEATED
DESCRIPTOR.message_types_by_name['TextRequest'] = _TEXTREQUEST
DESCRIPTOR.message_types_by_name['Releated'] = _RELEATED
DESCRIPTOR.message_types_by_name['TextResponse'] = _TEXTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextRequest = _reflection.GeneratedProtocolMessageType('TextRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEXTREQUEST,
  '__module__' : 'text_pb2'
  # @@protoc_insertion_point(class_scope:TextRequest)
  })
_sym_db.RegisterMessage(TextRequest)

Releated = _reflection.GeneratedProtocolMessageType('Releated', (_message.Message,), {
  'DESCRIPTOR' : _RELEATED,
  '__module__' : 'text_pb2'
  # @@protoc_insertion_point(class_scope:Releated)
  })
_sym_db.RegisterMessage(Releated)

TextResponse = _reflection.GeneratedProtocolMessageType('TextResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEXTRESPONSE,
  '__module__' : 'text_pb2'
  # @@protoc_insertion_point(class_scope:TextResponse)
  })
_sym_db.RegisterMessage(TextResponse)



_TEXTSERVICE = _descriptor.ServiceDescriptor(
  name='TextService',
  full_name='TextService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=153,
  serialized_end=220,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRelatedWords',
    full_name='TextService.GetRelatedWords',
    index=0,
    containing_service=None,
    input_type=_TEXTREQUEST,
    output_type=_TEXTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTSERVICE)

DESCRIPTOR.services_by_name['TextService'] = _TEXTSERVICE

# @@protoc_insertion_point(module_scope)
