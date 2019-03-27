# -*- encoding: utf-8 -*-

import dbus

from .const import *
from .core import Node

__all__ = [
    'ObjectManager',
    'AgentManager', 'ProfileManager', 'HealthManager',
    'GattManager', 'LEAdvertisingManager'
]

# ------------------------------------------------------------------------------
# --- Class ObjectManager -----------------------------------------------------
# ------------------------------------------------------------------------------

class ObjectManager(Node) :

    INTERFACE = DBUS_OM_INTERFACE

    def __init__(self, dbus_node=None) :
        if dbus_node is None :
            bus = dbus.SystemBus()
            path = '/'
            obj = bus.get_object(SERVICE_NAME, path)
            dbus_node = dbus.Interface(obj, self.INTERFACE)
        super().__init__(dbus_node)

    @property
    def managed_objects(self) :
        return self.GetManagedObjects()

    @property
    def paths(self) :
        return sorted(str(path) for path in self.managed_objects)
        
    

# ------------------------------------------------------------------------------
# --- Class BluezManager -----------------------------------------------------
# ------------------------------------------------------------------------------

class BluezManager(Node) :

    INTERFACE = BLUEZ_MANAGER_INTERFACE

    def __init__(self, dbus_node=None) :
        if dbus_node is None :
            bus = dbus.SystemBus()
            path = '/org/bluez'
            obj = bus.get_object(SERVICE_NAME, path)
            dbus_node = dbus.Interface(obj, self.INTERFACE)
        super().__init__(dbus_node)

# ------------------------------------------------------------------------------
# --- Class AgentManager -----------------------------------------------------
# ------------------------------------------------------------------------------

class AgentManager(BluezManager) :

    INTERFACE = AGENT_MANAGER_INTERFACE

# ------------------------------------------------------------------------------
# --- Class ProfileManager -----------------------------------------------------
# ------------------------------------------------------------------------------

class ProfileManager(BluezManager) :

    INTERFACE = PROFILE_MANAGER_INTERFACE

# ------------------------------------------------------------------------------
# --- Class HealthManager -----------------------------------------------------
# ------------------------------------------------------------------------------

class HealthManager(BluezManager) :

    INTERFACE = HEALTH_MANAGER_INTERFACE

# ------------------------------------------------------------------------------
# --- Class GattManager --------------------------------------------------------
# ------------------------------------------------------------------------------

class GattManager(Node) :

    INTERFACE = GATT_MANAGER_INTERFACE

# ------------------------------------------------------------------------------
# --- Class LEAdvertisingManager -----------------------------------------------
# ------------------------------------------------------------------------------

class LEAdvertisingManager(Node) :

    INTERFACE = LE_ADVERTISING_MANAGER_INTERFACE

