# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: autonomy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gps_pb2 as gps__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61utonomy.proto\x1a\tgps.proto\"!\n\x0f\x41utonomyCommand\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\xca\x01\n\x0c\x41utonomyData\x12$\n\x0b\x63oordinates\x18\x01 \x01(\x0b\x32\x0f.GpsCoordinates\x12\x0f\n\x07heading\x18\x02 \x01(\x02\x12\x1d\n\x05state\x18\x03 \x01(\x0e\x32\x0e.AutonomyState\x12\x19\n\x11raw_x_orientation\x18\x04 \x01(\x02\x12\x19\n\x11raw_y_orientation\x18\x05 \x01(\x02\x12\x19\n\x11raw_z_orientation\x18\x06 \x01(\x02\x12\x13\n\x04grid\x18\x07 \x01(\x0b\x32\x05.Grid\"\x1a\n\x04Grid\x12\x12\n\x04rows\x18\x01 \x03(\x0b\x32\x04.Row\"\x1f\n\x03Row\x12\x18\n\x10is_cell_occupied\x18\x01 \x03(\x08*a\n\rAutonomyState\x12\x1c\n\x18\x41UTONOMY_STATE_UNDEFINED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07PATHING\x10\x02\x12\x0f\n\x0b\x41PPROACHING\x10\x03\x12\x0b\n\x07\x41T_GATE\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'autonomy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTONOMYSTATE._serialized_start=330
  _AUTONOMYSTATE._serialized_end=427
  _AUTONOMYCOMMAND._serialized_start=29
  _AUTONOMYCOMMAND._serialized_end=62
  _AUTONOMYDATA._serialized_start=65
  _AUTONOMYDATA._serialized_end=267
  _GRID._serialized_start=269
  _GRID._serialized_end=295
  _ROW._serialized_start=297
  _ROW._serialized_end=328
# @@protoc_insertion_point(module_scope)
