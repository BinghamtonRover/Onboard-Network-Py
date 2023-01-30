# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protobuf/arm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12Protobuf/arm.proto\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"\xaf\x01\n\nArmCommand\x12\x1a\n\x07move_to\x18\x01 \x01(\x0b\x32\t.Position\x12\x11\n\tcalibrate\x18\x02 \x01(\x08\x12\x0e\n\x06swivel\x18\x03 \x01(\x02\x12\x0e\n\x06\x65xtend\x18\x04 \x01(\x02\x12\x0c\n\x04lift\x18\x05 \x01(\x02\x12\x16\n\x0eprecise_swivel\x18\x06 \x01(\x02\x12\x14\n\x0cprecise_lift\x18\x07 \x01(\x02\x12\x16\n\x0eprecise_extend\x18\x08 \x01(\x02\"D\n\x0bMotorStatus\x12\x11\n\tis_moving\x18\x01 \x01(\x08\x12\r\n\x05\x61ngle\x18\x02 \x01(\x02\x12\x13\n\x0btemperature\x18\x03 \x01(\x02\"\xa9\x01\n\x07\x41rmData\x12\"\n\x0f\x63urrentPosition\x18\x01 \x01(\x0b\x32\t.Position\x12!\n\x0etargetPosition\x18\x02 \x01(\x0b\x32\t.Position\x12\x1a\n\x04\x62\x61se\x18\x03 \x01(\x0b\x32\x0c.MotorStatus\x12\x1e\n\x08shoulder\x18\x04 \x01(\x0b\x32\x0c.MotorStatus\x12\x1b\n\x05\x65lbow\x18\x05 \x01(\x0b\x32\x0c.MotorStatus\"Y\n\x0bGripperData\x12\x10\n\x08rotation\x18\x01 \x01(\x02\x12\x0e\n\x06swivel\x18\x02 \x01(\x02\x12\r\n\x05pinch\x18\x03 \x01(\x02\x12\x19\n\x11motor_temperature\x18\x04 \x01(\x02\"q\n\x0eGripperCommand\x12\x11\n\tcalibrate\x18\x01 \x01(\x08\x12\r\n\x05pinch\x18\x02 \x01(\x02\x12\x0e\n\x06rotate\x18\x03 \x01(\x02\x12\x15\n\rprecise_pinch\x18\x04 \x01(\x02\x12\x16\n\x0eprecise_rotate\x18\x05 \x01(\x02\"J\n\x08HreiData\x12\x1a\n\x08\x61rm_data\x18\x01 \x01(\x0b\x32\x08.ArmData\x12\"\n\x0cgripper_data\x18\x02 \x01(\x0b\x32\x0c.GripperData\"Y\n\x0bHreiCommand\x12 \n\x0b\x61rm_command\x18\x01 \x01(\x0b\x32\x0b.ArmCommand\x12(\n\x0fgripper_command\x18\x02 \x01(\x0b\x32\x0f.GripperCommandb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Protobuf.arm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSITION._serialized_start=22
  _POSITION._serialized_end=65
  _ARMCOMMAND._serialized_start=68
  _ARMCOMMAND._serialized_end=243
  _MOTORSTATUS._serialized_start=245
  _MOTORSTATUS._serialized_end=313
  _ARMDATA._serialized_start=316
  _ARMDATA._serialized_end=485
  _GRIPPERDATA._serialized_start=487
  _GRIPPERDATA._serialized_end=576
  _GRIPPERCOMMAND._serialized_start=578
  _GRIPPERCOMMAND._serialized_end=691
  _HREIDATA._serialized_start=693
  _HREIDATA._serialized_end=767
  _HREICOMMAND._serialized_start=769
  _HREICOMMAND._serialized_end=858
# @@protoc_insertion_point(module_scope)
