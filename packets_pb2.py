# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='packets.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rpackets.proto\"\xaf\x01\n\nPacketInfo\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.PacketInfo.Type\x12\x0e\n\x06length\x18\x02 \x01(\x05\"q\n\x04Type\x12\x0e\n\nGAME_EVENT\x10\x00\x12\x0e\n\nPLAY_SOUND\x10\x01\x12\x11\n\rSOUND_REQUEST\x10\x02\x12\x12\n\x0eSOUND_RESPONSE\x10\x03\x12\x11\n\rCLIENT_UPDATE\x10\x04\x12\x0f\n\x0bSOUNDS_LIST\x10\x05\"\"\n\x0cSoundRequest\x12\x12\n\nsound_hash\x18\x01 \x03(\x0c\"+\n\rSoundResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\"\x9f\x02\n\tGameEvent\x12\x1f\n\x06update\x18\x01 \x01(\x0e\x32\x0f.GameEvent.Type\x12\x1b\n\x13proposed_sound_hash\x18\x02 \x01(\x0c\x12\x12\n\nkill_count\x18\x03 \x01(\x05\x12\r\n\x05round\x18\x04 \x01(\x05\"\xb0\x01\n\x04Type\x12\x07\n\x03MVP\x10\x00\x12\r\n\tROUND_WIN\x10\x01\x12\x0e\n\nROUND_LOSE\x10\x02\x12\x0b\n\x07SUICIDE\x10\x03\x12\x0c\n\x08TEAMKILL\x10\x04\x12\t\n\x05\x44\x45\x41TH\x10\x05\x12\t\n\x05\x46LASH\x10\x06\x12\t\n\x05KNIFE\x10\x07\x12\x0c\n\x08HEADSHOT\x10\x08\x12\x08\n\x04KILL\x10\t\x12\x0e\n\nCOLLATERAL\x10\n\x12\x0f\n\x0bROUND_START\x10\x0b\x12\x0b\n\x07TIMEOUT\x10\x0c\"\x9c\x01\n\x0c\x43lientUpdate\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.ClientUpdate.PlayerStatus\x12\x0b\n\x03map\x18\x02 \x01(\x0c\x12\x0f\n\x07steamid\x18\x03 \x01(\x06\x12\x12\n\nshard_code\x18\x04 \x01(\x0c\".\n\x0cPlayerStatus\x12\r\n\tCONNECTED\x10\x00\x12\x0f\n\x0bUNCONNECTED\x10\x01\"0\n\tPlaySound\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\nsound_hash\x18\x02 \x01(\x0c\x62\x06proto3')
)



_PACKETINFO_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='PacketInfo.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAME_EVENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAY_SOUND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUND_REQUEST', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUND_RESPONSE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_UPDATE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUNDS_LIST', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=80,
  serialized_end=193,
)
_sym_db.RegisterEnumDescriptor(_PACKETINFO_TYPE)

_GAMEEVENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='GameEvent.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MVP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_WIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_LOSE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUICIDE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEAMKILL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEATH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KNIFE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADSHOT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLATERAL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_START', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=12, number=12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=388,
  serialized_end=564,
)
_sym_db.RegisterEnumDescriptor(_GAMEEVENT_TYPE)

_CLIENTUPDATE_PLAYERSTATUS = _descriptor.EnumDescriptor(
  name='PlayerStatus',
  full_name='ClientUpdate.PlayerStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNCONNECTED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=677,
  serialized_end=723,
)
_sym_db.RegisterEnumDescriptor(_CLIENTUPDATE_PLAYERSTATUS)


_PACKETINFO = _descriptor.Descriptor(
  name='PacketInfo',
  full_name='PacketInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PacketInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='PacketInfo.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PACKETINFO_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=193,
)


_SOUNDREQUEST = _descriptor.Descriptor(
  name='SoundRequest',
  full_name='SoundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sound_hash', full_name='SoundRequest.sound_hash', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=195,
  serialized_end=229,
)


_SOUNDRESPONSE = _descriptor.Descriptor(
  name='SoundResponse',
  full_name='SoundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='SoundResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='SoundResponse.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=231,
  serialized_end=274,
)


_GAMEEVENT = _descriptor.Descriptor(
  name='GameEvent',
  full_name='GameEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='GameEvent.update', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposed_sound_hash', full_name='GameEvent.proposed_sound_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kill_count', full_name='GameEvent.kill_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='GameEvent.round', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GAMEEVENT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=564,
)


_CLIENTUPDATE = _descriptor.Descriptor(
  name='ClientUpdate',
  full_name='ClientUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientUpdate.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map', full_name='ClientUpdate.map', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steamid', full_name='ClientUpdate.steamid', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shard_code', full_name='ClientUpdate.shard_code', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTUPDATE_PLAYERSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=723,
)


_PLAYSOUND = _descriptor.Descriptor(
  name='PlaySound',
  full_name='PlaySound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='PlaySound.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sound_hash', full_name='PlaySound.sound_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=725,
  serialized_end=773,
)

_PACKETINFO.fields_by_name['type'].enum_type = _PACKETINFO_TYPE
_PACKETINFO_TYPE.containing_type = _PACKETINFO
_GAMEEVENT.fields_by_name['update'].enum_type = _GAMEEVENT_TYPE
_GAMEEVENT_TYPE.containing_type = _GAMEEVENT
_CLIENTUPDATE.fields_by_name['status'].enum_type = _CLIENTUPDATE_PLAYERSTATUS
_CLIENTUPDATE_PLAYERSTATUS.containing_type = _CLIENTUPDATE
DESCRIPTOR.message_types_by_name['PacketInfo'] = _PACKETINFO
DESCRIPTOR.message_types_by_name['SoundRequest'] = _SOUNDREQUEST
DESCRIPTOR.message_types_by_name['SoundResponse'] = _SOUNDRESPONSE
DESCRIPTOR.message_types_by_name['GameEvent'] = _GAMEEVENT
DESCRIPTOR.message_types_by_name['ClientUpdate'] = _CLIENTUPDATE
DESCRIPTOR.message_types_by_name['PlaySound'] = _PLAYSOUND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketInfo = _reflection.GeneratedProtocolMessageType('PacketInfo', (_message.Message,), dict(
  DESCRIPTOR = _PACKETINFO,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:PacketInfo)
  ))
_sym_db.RegisterMessage(PacketInfo)

SoundRequest = _reflection.GeneratedProtocolMessageType('SoundRequest', (_message.Message,), dict(
  DESCRIPTOR = _SOUNDREQUEST,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:SoundRequest)
  ))
_sym_db.RegisterMessage(SoundRequest)

SoundResponse = _reflection.GeneratedProtocolMessageType('SoundResponse', (_message.Message,), dict(
  DESCRIPTOR = _SOUNDRESPONSE,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:SoundResponse)
  ))
_sym_db.RegisterMessage(SoundResponse)

GameEvent = _reflection.GeneratedProtocolMessageType('GameEvent', (_message.Message,), dict(
  DESCRIPTOR = _GAMEEVENT,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:GameEvent)
  ))
_sym_db.RegisterMessage(GameEvent)

ClientUpdate = _reflection.GeneratedProtocolMessageType('ClientUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTUPDATE,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:ClientUpdate)
  ))
_sym_db.RegisterMessage(ClientUpdate)

PlaySound = _reflection.GeneratedProtocolMessageType('PlaySound', (_message.Message,), dict(
  DESCRIPTOR = _PLAYSOUND,
  __module__ = 'packets_pb2'
  # @@protoc_insertion_point(class_scope:PlaySound)
  ))
_sym_db.RegisterMessage(PlaySound)


# @@protoc_insertion_point(module_scope)
