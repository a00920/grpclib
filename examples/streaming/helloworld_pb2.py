# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming/helloworld.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streaming/helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1astreaming/helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbd\x02\n\x07Greeter\x12H\n\x12UnaryUnaryGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12K\n\x13UnaryStreamGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x30\x01\x12K\n\x13StreamUnaryGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00(\x01\x12N\n\x14StreamStreamGreeting\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00(\x01\x30\x01\x62\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='helloworld.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=70,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='helloworld.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'streaming.helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'streaming.helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=104,
  serialized_end=421,
  methods=[
  _descriptor.MethodDescriptor(
    name='UnaryUnaryGreeting',
    full_name='helloworld.Greeter.UnaryUnaryGreeting',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnaryStreamGreeting',
    full_name='helloworld.Greeter.UnaryStreamGreeting',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamUnaryGreeting',
    full_name='helloworld.Greeter.StreamUnaryGreeting',
    index=2,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamStreamGreeting',
    full_name='helloworld.Greeter.StreamStreamGreeting',
    index=3,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
