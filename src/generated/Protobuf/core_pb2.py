# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protobuf/core.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Protobuf/core.proto\"=\n\x07\x43onnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device\x12\x19\n\x08receiver\x18\x02 \x01(\x0e\x32\x07.Device\"%\n\nDisconnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device\"-\n\rUpdateSetting\x12\x1c\n\x06status\x18\x01 \x01(\x0e\x32\x0c.RoverStatus*d\n\x06\x44\x65vice\x12\x14\n\x10\x44\x45VICE_UNDEFINED\x10\x00\x12\r\n\tDASHBOARD\x10\x01\x12\x0e\n\nSUBSYSTEMS\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\x0c\n\x08\x41UTONOMY\x10\x04\x12\x0c\n\x08\x46IRMWARE\x10\x05*E\n\x0bRoverStatus\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\n\n\x06MANUAL\x10\x02\x12\x0e\n\nAUTONOMOUS\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Protobuf.core_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICE._serialized_start=172
  _DEVICE._serialized_end=272
  _ROVERSTATUS._serialized_start=274
  _ROVERSTATUS._serialized_end=343
  _CONNECT._serialized_start=23
  _CONNECT._serialized_end=84
  _DISCONNECT._serialized_start=86
  _DISCONNECT._serialized_end=123
  _UPDATESETTING._serialized_start=125
  _UPDATESETTING._serialized_end=170
# @@protoc_insertion_point(module_scope)