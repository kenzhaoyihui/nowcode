# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0bhello.proto\"\x1f\n\rActionRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\"!\n\x0e\x41\x63tionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t23\n\x06\x41\x63tion\x12)\n\x04hihi\x12\x0e.ActionRequest\x1a\x0f.ActionResponse\"\x00\x62\x06proto3')
)




_ACTIONREQUEST = _descriptor.Descriptor(
  name='ActionRequest',
  full_name='ActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='ActionRequest.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=46,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ActionResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['ActionRequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONREQUEST,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:ActionRequest)
  ))
_sym_db.RegisterMessage(ActionRequest)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONRESPONSE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:ActionResponse)
  ))
_sym_db.RegisterMessage(ActionResponse)



_ACTION = _descriptor.ServiceDescriptor(
  name='Action',
  full_name='Action',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=83,
  serialized_end=134,
  methods=[
  _descriptor.MethodDescriptor(
    name='hihi',
    full_name='Action.hihi',
    index=0,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACTION)

DESCRIPTOR.services_by_name['Action'] = _ACTION

# @@protoc_insertion_point(module_scope)