# -*- encoding: utf-8 -*-

import struct
import dbus

from ..vendors import getService
from ..utils import (
    get_managed_objects,
    list_properties, get_property, set_property,
    list_interfaces, list_nodes, list_methods, list_signals,
    introspect_dump
)

from .const import *
from .exceptions import NodeInterfaceError

__all__ = [ 'Node', 'Peripheral', 'SimAccess' ]

# ------------------------------------------------------------------------------
# --- Class Node ---------------------------------------------------------------
# ------------------------------------------------------------------------------

class Node :

    INTERFACE = INTROSPECTABLE_INTERFACE

    def __init__(self, dbus_node, interface=None) :
        bus = dbus.SystemBus()
        path = dbus_node.object_path
        obj = bus.get_object(SERVICE_NAME, path)
        if interface is None :
            interface = self.INTERFACE
        if interface not in list_interfaces(obj) :
            raise NodeInterfaceError('Bad interface : {}'.format(interface))
        node = dbus.Interface(obj, interface)
        self.__dict__['_dbus_node'] = node

    @classmethod
    def make(cls, path, interface=None, service=SERVICE_NAME) :
        bus = dbus.SystemBus()
        obj = bus.get_object(service, path)
        return cls(obj, interface)
    
    def __repr__(self) :
        return '<{} {}@{}>'.format(
            self.__class__.__name__,
            self._dbus_node.object_path,
            self.interface
        )

    def __getattr__(self, name) :
        if name in self.properties :
            return get_property(self._dbus_node, name)
        if name in self.methods :
            return self._dbus_node.get_dbus_method(name)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(
                self.__class__.__name__, name
            )
        )

    def __setattr__(self, name, value) :
        if name in self.properties :
            if 'readwrite' in self.properties[name] :
                set_property(self._dbus_node, name, value)
            else :
                raise AttributeError("'{}' attribute is read only".format(name))    
        else :
            super().__setattr__(name, value)

    @property
    def interface(self) :
        return self._dbus_node.dbus_interface

    @property
    def object_path(self) :
        return self._dbus_node.object_path

    @property
    def interfaces(self) :
        return list_interfaces(self._dbus_node)

    @property
    def properties(self) :
        return list_properties(self._dbus_node)

    @property
    def methods(self) :
        return list_methods(self._dbus_node)

    @property
    def signals(self) :
        return list_signals(self._dbus_node)

    @property
    def nodenames(self) :
        return list_nodes(self._dbus_node)

    @property
    def nodes(self) :
        return list(
            Node.make(path, interface)
            for node in list_nodes(self._dbus_node)
            for path in ['/'.join([self.object_path, node])]
            for interface in get_managed_objects()[path]
            if interface.startswith(SERVICE_NAME)
        )

    @property
    def adapter(self) :
        return Node.make(self.Adapter, ADAPTER_INTERFACE)

    @property
    def device(self) :
        return Node.make(self.Device, DEVICE_INTERFACE)
            
    def introspect(self, dump=False, recurse=False, only_properties=False) :
        if dump :
            return introspect_dump(
                dest=SERVICE_NAME,
                path=self.object_path,
                recurse=recurse,
                only_properties=only_properties
            )
        bus = dbus.SystemBus()
        path = self.object_path
        obj = bus.get_object(SERVICE_NAME, path)
        dbus_node = dbus.Interface(obj, INTROSPECTABLE_INTERFACE)
        return str(dbus_node.Introspect())

# ------------------------------------------------------------------------------
# --- Class Peripheral ---------------------------------------------------------
# ------------------------------------------------------------------------------

class Peripheral(Node) :

    INTERFACE = PERIPHERAL_INTERFACE

    def __repr__(self) :
        return '<{} [{}] {}>'.format(
            self.__class__.__name__,
            self.address,
            self.alias
        )

    @property
    def name(self) :
        try :
            name = str(self.Name)
        except dbus.DBusException :
            name = '(unknown)'
        return name
    
    @property
    def alias(self) :
        return str(self.Alias)

    @alias.setter
    def alias(self, alias) :
        self.Alias = alias

    @property
    def modalias(self) :
        return str(self.Modalias)

    @property
    def class_(self) :
        try :
            cls = int(self.Class)
        except dbus.DBusException :
            cls = 0
        return cls

    @property
    def address(self) :
        return str(self.Address)

    @property
    def uuids(self) :
        return list(str(uuid) for uuid in self.UUIDs)

    def present(self) :
        print('[{}] {}'.format(self.address, self.alias))
        print('\tClass : 0x{:06x}'.format(self.class_))
        for u in self.uuids :
            print('\t[{}] {}'.format(u, getService(u)))

# ------------------------------------------------------------------------------
# --- Class SimAccess ----------------------------------------------------------
# ------------------------------------------------------------------------------

class SimAccess(Node) :

    INTERFACE = SIM_ACCESS_INTERFACE

