# -*- encoding: utf-8 -*-

import dbus

from .const import *
from .core import Peripheral
from .media import MediaControl, MediaPlayer, MediaTransport
from .network import Network
from .input import Input
from .gatt import GattService

__all__ = [ 'Device' ]

# ------------------------------------------------------------------------------
# --- Class Device -------------------------------------------------------------
# ------------------------------------------------------------------------------

class Device(Peripheral) :

    INTERFACE = DEVICE_INTERFACE

    @property
    def mediaControl(self) :
        return MediaControl(self)

    @property
    def mediaPlayer(self) :
        return MediaPlayer(
            next(
                node
                for node in self.nodes
                if node.interface == MEDIA_PLAYER_INTERFACE
            )
        )

    @property
    def mediaTransport(self) :
        return MediaTransport(
            next(
                node
                for node in self.nodes
                if node.interface == MEDIA_TRANSPORT_INTERFACE
            )
        )
    
    @property
    def input(self) :
        return Input(self)

    @property
    def network(self) :
        return Network(self)

    @property
    def icon(self) :
        try :
            return str(self.Icon)
        except dbus.DBusException :
            return '(none)'

    @property
    def rssi(self) :
        try :
            return int(self.RSSI)
        except dbus.DBusException :
            pass

    @property
    def connected(self) :
        return bool(self.Connected)

    @property
    def paired(self) :
        return bool(self.Paired)

    @property
    def legacypairing(self) :
        return bool(self.LegacyPairing)

    @property
    def trusted(self) :
        return bool(self.Trusted)

    @trusted.setter
    def trusted(self, trusted) :
        self.Trusted = trusted

    @property
    def blocked(self) :
        return bool(self.Blocked)

    @blocked.setter
    def blocked(self, blocked) :
        self.Blocked = blocked

    @property
    def services(self) :
        return list(
            GattService(node)
            for node in self.nodes
            if node.interface == GATT_SERVICE_INTERFACE
        )

    @property
    def primary(self) :
        return list(
            service
            for service in self.services
            if service.Primary
        )

    @property
    def characteristics(self) :
        return list(
            charac
            for service in self.services
            for charac in service.characteristics
        )

    @property
    def descriptors(self) :
        return list(
            desc
            for service in self.services
            for charac in service.characteristics
            for desc in charac.descriptors
        )

    def present_gatt(self) :
        for service in self.services :
            service.present()

