# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\x12\x04\x64\x65mo\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\rAppendRequest\x12\r\n\x05value\x18\x01 \x01(\t\"\x1d\n\x0b\x41ppendReply\x12\x0e\n\x06values\x18\x01 \x03(\t2k\n\x04\x44\x65mo\x12/\n\x05Hello\x12\x12.demo.HelloRequest\x1a\x10.demo.HelloReply\"\x00\x12\x32\n\x06\x41ppend\x12\x13.demo.AppendRequest\x1a\x11.demo.AppendReply\"\x00\x42$Z\"github.com/dimartiro/grpc-examplesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\"github.com/dimartiro/grpc-examples'
  _HELLOREQUEST._serialized_start=20
  _HELLOREQUEST._serialized_end=48
  _HELLOREPLY._serialized_start=50
  _HELLOREPLY._serialized_end=79
  _APPENDREQUEST._serialized_start=81
  _APPENDREQUEST._serialized_end=111
  _APPENDREPLY._serialized_start=113
  _APPENDREPLY._serialized_end=142
  _DEMO._serialized_start=144
  _DEMO._serialized_end=251
# @@protoc_insertion_point(module_scope)