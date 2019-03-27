# -*- encoding: utf-8 -*-

import dbus

from .const import *
from .core import Node

__all__ = [
    'Media',
    'MediaControl',
    'MediaPlayer', 'MediaTransport'
]

# ------------------------------------------------------------------------------
# --- Class Media --------------------------------------------------------------
# ------------------------------------------------------------------------------

class Media(Node) :

    INTERFACE = MEDIA_INTERFACE


# ------------------------------------------------------------------------------
# --- Class MediaControl -------------------------------------------------------
# ------------------------------------------------------------------------------

class MediaControl(Node) :

    INTERFACE = MEDIA_CONTROL_INTERFACE

    @property
    def connected(self) :
        return bool(self.Connected)

    @property
    def player(self) :
        bus = dbus.SystemBus()
        obj = bus.get_object(SERVICE_NAME, self.Player)
        return MediaPlayer(obj)

# ------------------------------------------------------------------------------
# --- Class MediaPlayer --------------------------------------------------------
# ------------------------------------------------------------------------------

class MediaPlayer(Node) :

    INTERFACE = MEDIA_PLAYER_INTERFACE

    @property
    def position(self) :
        return int(self.Position)

    @property
    def status(self) :
        return str(self.Status)

    @property
    def repeat(self) :
        try :
            return str(self.Repeat)
        except dbus.DBusException :
            return '(none)'

    @repeat.setter
    def repeat(self, repeat) :
        self.Repeat = repeat
        
    @property
    def shuffle(self) :
        try :
            return str(self.Shuffle)
        except dbus.DBusException :
            return '(none)'

    @shuffle.setter
    def shuffle(self, shuffle) :
        self.Shuffle = shuffle
        

    def present(self) :
        print('Status : {}'.format(self.status))
        print('Current track :')
        for k,v in self.Track.items() :
            print('  {}: {}'.format(k, v))
        print('Repeat : {}'.format(self.repeat))
        print('Shuffle : {}'.format(self.shuffle))

# ------------------------------------------------------------------------------
# --- Class MediaTransport -----------------------------------------------------
# ------------------------------------------------------------------------------

class MediaTransport(Node) :

    INTERFACE = MEDIA_TRANSPORT_INTERFACE

    @property
    def uuid(self) :
        return str(self.UUID)

    @property
    def state(self) :
        return str(self.State)

    @property
    def codec(self) :
         return struct.pack('B', self.Codec)

    @property
    def configuration(self) :
        return bytes(self.Configuration)

    @property
    def volume(self) :
        return int(self.Volume)

    @volume.setter
    def volume(self, level) :
        self.Volume = dbus.UInt16(level % 128)

