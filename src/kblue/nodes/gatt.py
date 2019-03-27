# -*- encoding: utf-8 -*-

import dbus

from ..vendors import getService

from .const import *
from .core import Node

__all__ = [ 'GattService', 'GattCharacteristic', 'GattDescriptor' ]

# ------------------------------------------------------------------------------
# --- Class GattService --------------------------------------------------------
# ------------------------------------------------------------------------------

class GattService(Node) :

    INTERFACE = GATT_SERVICE_INTERFACE

    @property
    def name(self) :
        return self.object_path.split('/')[-1]

    @property
    def handle(self) :
        return int(self.name.split('service')[-1], 16)

    @property
    def device(self) :
        return Node.make(self.Device, DEVICE_INTERFACE)

    @property
    def characteristics(self) :
        return list(
            GattCharacteristic(node)
            for node in self.nodes
            if node.interface == GATT_CHARACTERISTIC_INTERFACE
        )

    @property
    def descriptors(self) :
        return list(
            GattDescriptor(desc)
            for charac in self.characteristics
            for desc in charac.descriptors
        )

    def present(self) :
        print('Service[0x{:04x}] : {} [{}]'.format(
            self.handle, getService(self.UUID), self.UUID
        ))
        for char in self.characteristics :
            char.present()

# ------------------------------------------------------------------------------
# --- Class GattCharacteristic -------------------------------------------------
# ------------------------------------------------------------------------------

class GattCharacteristic(Node) :

    INTERFACE = GATT_CHARACTERISTIC_INTERFACE

    @property
    def name(self) :
        return self.object_path.split('/')[-1]

    @property
    def value(self) :
        return bytes(self.Value)

    @property
    def handle(self) :
        return int(self.name.split('char')[-1], 16)

    @property
    def uuid(self) :
        return str(self.UUID)

    @property
    def service(self) :
        try :
            return GattService.make(self.Service)
        except AttributeError :
            return self.characteristic.service

    @property
    def characteristic(self) :
        try :
            return GattCharacteristic.make(self.Characteristic)
        except AttributeError :
            return self

    @property
    def flags(self) :
        try :
            return list(
                str(flag)
                for flag in self.Flags
            )
        except AttributeError :
            return list()

    @property
    def notifying(self) :
        try :
            return bool(self.Notifying)
        except AttributeError :
            pass

    @property
    def writeAcquired(self) :
        try :
            return bool(self.WriteAcquired)
        except AttributeError :
            pass

    @property
    def notifyAcquired(self) :
        try :
            return bool(self.NotifyAcquired)
        except AttributeError :
            pass

    def read(self, options={}) :
        return bytes(self.ReadValue(options))

    def write(self, data, options={}) :
        self.WriteValue(data, options)

    @property
    def descriptors(self) :
        return list(
            GattDescriptor(node)
            for node in self.nodes
            if node.interface == GATT_DESCRIPTOR_INTERFACE
        )

    def present(self) :
        print('\tCharacteristic[0x{:04x}] : {} [{}]'.format(
            self.handle, getService(self.UUID), self.UUID
        ))
        print('\t-> Flags : {}'.format(', '.join(self.flags)))
        for descriptor in self.descriptors :
            descriptor.present()

# ------------------------------------------------------------------------------
# --- Class GattDescriptor -----------------------------------------------------
# ------------------------------------------------------------------------------

class GattDescriptor(GattCharacteristic) :

    INTERFACE = GATT_DESCRIPTOR_INTERFACE

    @property
    def handle(self) :
        return int(self.name.split('desc')[-1], 16)

    def present(self) :
        print('\t\tDescriptor[0x{:04x}] : {} [{}]'.format(
            self.handle, getService(self.UUID), self.UUID
        ))
