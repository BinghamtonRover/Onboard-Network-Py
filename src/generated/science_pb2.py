# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: science.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import version_pb2 as version__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rscience.proto\x1a\rversion.proto\"\xb9\x02\n\x0eScienceCommand\x12\x16\n\x0e\x63\x61rousel_motor\x18\x01 \x01(\x02\x12\x13\n\x0bscoop_motor\x18\x02 \x01(\x02\x12\x18\n\x10subsurface_motor\x18\x03 \x01(\x02\x12\x19\n\x05pumps\x18\x04 \x01(\x0e\x32\n.PumpState\x12\x1b\n\x06\x66unnel\x18\x05 \x01(\x0e\x32\x0b.ServoState\x12\x1a\n\x05scoop\x18\x06 \x01(\x0e\x32\x0b.ServoState\x12\"\n\x08\x63\x61rousel\x18\x07 \x01(\x0e\x32\x10.CarouselCommand\x12\x11\n\tcalibrate\x18\x08 \x01(\x08\x12\x0c\n\x04stop\x18\t \x01(\x08\x12\x0e\n\x06sample\x18\n \x01(\x05\x12\x1c\n\x05state\x18\x0b \x01(\x0e\x32\r.ScienceState\x12\x19\n\x07version\x18\x0c \x01(\x0b\x32\x08.Version\"\x8a\x01\n\x0bScienceData\x12\x0e\n\x06sample\x18\x01 \x01(\x05\x12\x1c\n\x05state\x18\x02 \x01(\x0e\x32\r.ScienceState\x12\x0b\n\x03\x63o2\x18\x03 \x01(\x02\x12\x10\n\x08humidity\x18\x04 \x01(\x02\x12\x13\n\x0btemperature\x18\x05 \x01(\x02\x12\x19\n\x07version\x18\x06 \x01(\x0b\x32\x08.Version*H\n\nServoState\x12\x19\n\x15SERVO_STATE_UNDEFINED\x10\x00\x12\x0e\n\nSERVO_OPEN\x10\x01\x12\x0f\n\x0bSERVO_CLOSE\x10\x02*J\n\tPumpState\x12\x18\n\x14PUMP_STATE_UNDEFINED\x10\x00\x12\x0b\n\x07PUMP_ON\x10\x01\x12\x0c\n\x08PUMP_OFF\x10\x02\x12\x08\n\x04\x46ILL\x10\x03*R\n\x0cScienceState\x12\x1b\n\x17SCIENCE_STATE_UNDEFINED\x10\x00\x12\x10\n\x0c\x43OLLECT_DATA\x10\x01\x12\x13\n\x0fSTOP_COLLECTING\x10\x02*\x94\x01\n\x0f\x43\x61rouselCommand\x12\x1e\n\x1a\x43\x41ROUSEL_COMMAND_UNDEFINED\x10\x00\x12\r\n\tNEXT_TUBE\x10\x01\x12\r\n\tPREV_TUBE\x10\x02\x12\x10\n\x0cNEXT_SECTION\x10\x03\x12\x10\n\x0cPREV_SECTION\x10\x04\x12\r\n\tFILL_TUBE\x10\x05\x12\x10\n\x0c\x46ILL_SECTION\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'science_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVOSTATE']._serialized_start=489
  _globals['_SERVOSTATE']._serialized_end=561
  _globals['_PUMPSTATE']._serialized_start=563
  _globals['_PUMPSTATE']._serialized_end=637
  _globals['_SCIENCESTATE']._serialized_start=639
  _globals['_SCIENCESTATE']._serialized_end=721
  _globals['_CAROUSELCOMMAND']._serialized_start=724
  _globals['_CAROUSELCOMMAND']._serialized_end=872
  _globals['_SCIENCECOMMAND']._serialized_start=33
  _globals['_SCIENCECOMMAND']._serialized_end=346
  _globals['_SCIENCEDATA']._serialized_start=349
  _globals['_SCIENCEDATA']._serialized_end=487
# @@protoc_insertion_point(module_scope)
