# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/visualization_msgs/Marker.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from datatypes.ros import builtins_pb2 as ros_dot_builtins__pb2
from datatypes.ros.geometry_msgs import Point_pb2 as ros_dot_geometry__msgs_dot_Point__pb2
from datatypes.ros.geometry_msgs import Pose_pb2 as ros_dot_geometry__msgs_dot_Pose__pb2
from datatypes.ros.geometry_msgs import Vector3_pb2 as ros_dot_geometry__msgs_dot_Vector3__pb2
from datatypes.ros.std_msgs import ColorRGBA_pb2 as ros_dot_std__msgs_dot_ColorRGBA__pb2
from datatypes.ros.std_msgs import Header_pb2 as ros_dot_std__msgs_dot_Header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ros/visualization_msgs/Marker.proto',
  package='ros.visualization_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n#ros/visualization_msgs/Marker.proto\x12\x16ros.visualization_msgs\x1a\x12ros/builtins.proto\x1a\x1dros/geometry_msgs/Point.proto\x1a\x1cros/geometry_msgs/Pose.proto\x1a\x1fros/geometry_msgs/Vector3.proto\x1a\x1cros/std_msgs/ColorRGBA.proto\x1a\x19ros/std_msgs/Header.proto\"\xb2\x03\n\x06Marker\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.ros.std_msgs.Header\x12\n\n\x02ns\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\x05\x12%\n\x04pose\x18\x06 \x01(\x0b\x32\x17.ros.geometry_msgs.Pose\x12)\n\x05scale\x18\x07 \x01(\x0b\x32\x1a.ros.geometry_msgs.Vector3\x12&\n\x05\x63olor\x18\x08 \x01(\x0b\x32\x17.ros.std_msgs.ColorRGBA\x12\x1f\n\x08lifetime\x18\t \x01(\x0b\x32\r.ros.Duration\x12\x14\n\x0c\x66rame_locked\x18\n \x01(\x08\x12(\n\x06points\x18\x0b \x03(\x0b\x32\x18.ros.geometry_msgs.Point\x12\'\n\x06\x63olors\x18\x0c \x03(\x0b\x32\x17.ros.std_msgs.ColorRGBA\x12\x0c\n\x04text\x18\r \x01(\t\x12\x15\n\rmesh_resource\x18\x0e \x01(\t\x12#\n\x1bmesh_use_embedded_materials\x18\x0f \x01(\x08\x62\x06proto3'
  ,
  dependencies=[ros_dot_builtins__pb2.DESCRIPTOR,ros_dot_geometry__msgs_dot_Point__pb2.DESCRIPTOR,ros_dot_geometry__msgs_dot_Pose__pb2.DESCRIPTOR,ros_dot_geometry__msgs_dot_Vector3__pb2.DESCRIPTOR,ros_dot_std__msgs_dot_ColorRGBA__pb2.DESCRIPTOR,ros_dot_std__msgs_dot_Header__pb2.DESCRIPTOR,])




_MARKER = _descriptor.Descriptor(
  name='Marker',
  full_name='ros.visualization_msgs.Marker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ros.visualization_msgs.Marker.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ns', full_name='ros.visualization_msgs.Marker.ns', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ros.visualization_msgs.Marker.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ros.visualization_msgs.Marker.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='ros.visualization_msgs.Marker.action', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='ros.visualization_msgs.Marker.pose', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='ros.visualization_msgs.Marker.scale', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='ros.visualization_msgs.Marker.color', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime', full_name='ros.visualization_msgs.Marker.lifetime', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_locked', full_name='ros.visualization_msgs.Marker.frame_locked', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='ros.visualization_msgs.Marker.points', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colors', full_name='ros.visualization_msgs.Marker.colors', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='ros.visualization_msgs.Marker.text', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_resource', full_name='ros.visualization_msgs.Marker.mesh_resource', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_use_embedded_materials', full_name='ros.visualization_msgs.Marker.mesh_use_embedded_materials', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=235,
  serialized_end=669,
)

_MARKER.fields_by_name['header'].message_type = ros_dot_std__msgs_dot_Header__pb2._HEADER
_MARKER.fields_by_name['pose'].message_type = ros_dot_geometry__msgs_dot_Pose__pb2._POSE
_MARKER.fields_by_name['scale'].message_type = ros_dot_geometry__msgs_dot_Vector3__pb2._VECTOR3
_MARKER.fields_by_name['color'].message_type = ros_dot_std__msgs_dot_ColorRGBA__pb2._COLORRGBA
_MARKER.fields_by_name['lifetime'].message_type = ros_dot_builtins__pb2._DURATION
_MARKER.fields_by_name['points'].message_type = ros_dot_geometry__msgs_dot_Point__pb2._POINT
_MARKER.fields_by_name['colors'].message_type = ros_dot_std__msgs_dot_ColorRGBA__pb2._COLORRGBA
DESCRIPTOR.message_types_by_name['Marker'] = _MARKER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Marker = _reflection.GeneratedProtocolMessageType('Marker', (_message.Message,), {
  'DESCRIPTOR' : _MARKER,
  '__module__' : 'ros.visualization_msgs.Marker_pb2'
  # @@protoc_insertion_point(class_scope:ros.visualization_msgs.Marker)
  })
_sym_db.RegisterMessage(Marker)


# @@protoc_insertion_point(module_scope)