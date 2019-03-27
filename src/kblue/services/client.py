# -*- encoding: utf-8 -*-

import kblue
from .core import DBusBase

__all__ = [ 'DBusClient', 'BluetoothDevice' ]

# ------------------------------------------------------------------------------
# --- class BDusClient ---------------------------------------------------------
# ------------------------------------------------------------------------------

class DBusClient(DBusBase) :
    pass

# ------------------------------------------------------------------------------
# --- class BluetoothDevice ----------------------------------------------------
# ------------------------------------------------------------------------------

class BluetoothDevice(DBusBase) :

    def __init__(self, device) :
        self._device = device
        super().__init__()
        self._setup()

    @property
    def device(self) :
        return self._device

    def _setup(self) :
        self.logger.debug('{} _setup'.format(self.device))
        self.setup()

    def connect(self) :
        self.logger.debug('{} connect'.format(self.device))
        self.device.Connect()

    def disconnect(self) :
        self.logger.debug('{} disconnect'.format(self.device))
        self.device.Disconnect()

    def listen_to_signals(self) :
        super().listen_to_signals()
        self.bus.get_system().add_signal_receiver(
            self.propertiesChanged,
            bus_name = 'org.bluez',
            dbus_interface = 'org.freedesktop.DBus.Properties',
            signal_name = 'PropertiesChanged',
            path_keyword = 'path'
        )

    def propertiesChanged(self, interface, changed, invalidated, path) :
        if self.device.object_path in path :            
            for name, value in changed.items() :
                    
                if interface == kblue.DEVICE_INTERFACE :
                    if name == 'Connected' :
                        if value == 1 :
                            self.logger.debug('{} connected'.format(self.device))
                            self.connected()
                        else :
                            self.logger.debug('{} disconnected'.format(self.device))
                            self.disconnected()
                    if name == 'ServicesResolved' :
                        if value == 1 :
                            self.logger.debug('{} services resolved'.format(self.device))
                            self.services_resolved()
                        
                elif interface == kblue.GATT_CHARACTERISTIC_INTERFACE :
                    if name == 'Value' :
                        charac = next(
                            char
                            for char in self.device.characteristics
                            if char.object_path == path
                        )
                        self.logger.debug('{} updated -> {}'.format(
                                charac, value
                            )
                        )
                        self.characteristic_updated(charac)
                
    def setup(self) :
        pass

    def connected(self) :
        pass

    def disconnected(self) :
        pass

    def services_resolved(self) :
        pass

    def characteristic_updated(self, characteristic) :
        pass
