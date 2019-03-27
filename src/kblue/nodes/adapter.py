# -*- encoding: utf-8 -*-

from ..utils import find_adapter

from .const import *
from .core import Peripheral, SimAccess
from .managers import GattManager, LEAdvertisingManager
from .device import Device
from .network import NetworkServer
from .media import Media

__all__ = [ 'Adapter' ]

# ------------------------------------------------------------------------------
# --- Class Adapter ------------------------------------------------------------
# ------------------------------------------------------------------------------

class Adapter(Peripheral) :

    INTERFACE = ADAPTER_INTERFACE

    def __init__(self, dbus_node=None) :
        if dbus_node is None or isinstance(dbus_node, str) :
            dbus_node = find_adapter(dbus_node)
        super().__init__(dbus_node)

    @property
    def devices(self) :
        return list(
            Device(node)
            for node in self.nodes
            if node.interface == DEVICE_INTERFACE
        )

    @property
    def connected_devices(self) :
        return [
            device
            for device in self.devices
            if device.connected
        ]
    
    @property
    def paired_devices(self) :
        return [
            device
            for device in self.devices
            if device.paired
        ]

    @property
    def trusted_devices(self) :
        return [
            device
            for device in self.devices
            if device.trusted
        ]

    @property
    def blocked_devices(self) :
        return [
            device
            for device in self.devices
            if device.blocked
        ]

    @property
    def discovering(self) :
        return bool(self.Discovering)

    @property
    def powered(self) :
        return bool(self.Powered)

    @powered.setter
    def powered(self, powered) :
        self.Powered = powered

    @property
    def pairable(self) :
        return bool(self.Pairable)

    @pairable.setter
    def pairable(self, pairable) :
        self.Pairable = pairable
        
    @property
    def networkServer(self) :
        return NetworkServer(self)

    @property
    def gattManager(self) :
        return GattManager(self)

    @property
    def leAdvertisingManager(self) :
        return LEAdvertisingManager(self)

    @property
    def media(self) :
        return Media(self)

    @property
    def simAccess(self) :
        return SimAccess(self)

    def get_device(self, bdaddr_or_alias) :
        return next(
            device
            for device in self.devices
            if device.Address == bdaddr_or_alias
            or device.Alias == bdaddr_or_alias
            or device.name== bdaddr_or_alias
        )            

    def present(self) :
        super().present()
        print('\tpowered : {}'.format(self.powered))
        print('\tdiscovering : {}'.format(self.discovering))
        print('\tpairable : {}'.format(self.pairable))
        print('\tdevices :')
        for dev in self.devices :
            print('\t\t{}'.format(dev))
