# -*- encoding: utf-8 -*-

import logging
import dbus.service

from .core import DBusBase

__all__ = [ 'DBusService', 'Service' ]

# ------------------------------------------------------------------------------
# --- class DBusService --------------------------------------------------------
# ------------------------------------------------------------------------------

class DBusService(DBusBase) :

    def __init__(self, bus_name) :
        super().__init__()
        self._bus_name = dbus.service.BusName(
            bus_name,
            bus=self._bus,
            do_not_queue=True
        )
        self._services = []

    @property
    def services(self) :
        return self._services

    def add_service(self, service_object) :
        if issubclass(service_object, dbus.service.Object) :
            service = service_object(self._bus_name)
            service.loop = self._loop
            self._services.append(service)
            return service

    def remove_service(self, service_instance) :
        if service_instance in self.services :
            for conn, path, flag in service_instance.locations :
                service_instance.remove_from_connection(conn, path)
            self.services.remove(service_instance)
            return True
        return False
            
# ------------------------------------------------------------------------------
# --- class Service ------------------------------------------------------------
# ------------------------------------------------------------------------------

class Service(dbus.service.Object):

    PATH = '/com/kblue'

    def __init__(self, bus_name):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._bus = bus_name.get_bus()
        self._loop = None
        super().__init__(bus_name, self.PATH)
        self.logger.debug(
            'bus : {} {} [{}]'.format(
                self._bus,
                bus_name.get_name(),
                self._bus.get_unique_name()
            )
        )
        self.logger.debug('path : {}'.format(self._object_path))
        
    @property
    def bus(self) :
        return self._bus

    @property
    def loop(self) :
        return self._loop

    @loop.setter
    def loop(self, loop) :
        self._loop = loop

    @dbus.service.method(
        dbus_interface='com.kblue.Service',
        out_signature='s',
        sender_keyword='sender'
    )
    def Ping(self, sender=None):
        self.logger.debug('method=Ping, sender={}'.format(sender))
        self.PingResponse(sender)
        return sender

    @dbus.service.signal(
        dbus_interface='com.kblue.Service',
        signature='s'
    )
    def PingResponse(self, sender) :
        self.logger.debug('signal=PingResponse, sender={}'.format(sender))
