# -*- encoding: utf-8 -*-

import logging
import threading
import dbus, dbus.service
import dbus.mainloop.glib
from gi.repository import GObject

from .exceptions import DBusSessionError
from .helpers import (
    dbus_session_bus_address, display,
    build_signal
)

__all__ = [ 'DBusBase', 'Signal' ]

# ------------------------------------------------------------------------------
# --- Bootstrap ----------------------------------------------------------------
# ------------------------------------------------------------------------------

# logging at module level
logger = logging.getLogger(__name__)

# Check prerequisites for dbus session
if dbus_session_bus_address() is None and display() is None :
    message = "Can't find a session : no DISPLAY or DBUS_SESSION_BUS_ADDRESS"
    logger.error(message)
    raise DBusSessionError(message)
logger.debug('DBUS_SESSION_BUS_ADDRESS={}'.format(dbus_session_bus_address()))
logger.debug('DISPLAY={}'.format(display()))

# Initialize mainloop
logger.debug('initialize mainloop')
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
dbus.mainloop.glib.threads_init()

# ------------------------------------------------------------------------------
# --- class DBusBase -----------------------------------------------------------
# ------------------------------------------------------------------------------

class DBusBase :

    def __init__(self) :
        self.logger = logging.getLogger(self.__class__.__name__)
        self._loop = GObject.MainLoop()
        self._bus = dbus.SessionBus()
        self._thread = None
        self.logger.debug('session Bus {}'.format(self.bus_unique_name))
        self.listen_to_signals()

    def __enter__(self) :
        self.run(detached=True)
        return self

    def __exit__(self, exc_type, exc_value, traceback) :
        self.quit()
        return True

    @property
    def bus(self) :
        return self._bus

    @property
    def bus_unique_name(self) :
        return self._bus.get_unique_name()

    @property
    def running(self) :
        if self._thread is not None :
            return self._thread.is_alive()
        return False

    def listen_to_signals(self) :
        self.bus.add_signal_receiver(
            self.quit,
            dbus_interface='com.kblue.Mainloop',
            signal_name='Stop'
        )

    def send_signal(self, signal_fqname, *args, signature=None, path='/com/kblue/signal') :
        dbus_interface, point, signal_name = signal_fqname.rpartition('.')
        signal_func = build_signal(signal_name, len(args))
        signal_emit = dbus.service.signal(
            dbus_interface=dbus_interface,
            signature=signature
        )

        with Signal(self.bus, path) as signal :
            signal_emit(signal_func)(signal, *args)

    def timeout_add_seconds(self, duration, callback, *args) :
        GObject.timeout_add_seconds(duration, callback, *args)

    def run(self, detached=False) :
        self._thread = threading.Thread(target=self._run)
        self._thread.start()
        self.logger.debug('start : {}'.format(self._thread))
        if not detached :
            self.join()

    def _run(self) :
        try :
            self._loop.run()
        except KeyboardInterrupt :
            self.logger.warning('keyboard interrupt received')
        except Exception as e :
            self.logger.error("unexpected exception occurred: '{}'".format(str(e)))
        finally :
            self.quit()

    def join(self, timeout=None) :
        if self._thread is not None :
            self._thread.join(timeout)


    def quit(self, *args) :
        if self._loop.is_running() :
            self.logger.debug('exit mainloop')
            self._loop.quit()

    def stop(self) :
        self.quit()
        
# ------------------------------------------------------------------------------
# --- class Signal -------------------------------------------------------------
# ------------------------------------------------------------------------------

class Signal(dbus.service.Object) :

    def __init__(self, bus, path) :
        super().__init__()
        self._bus = bus
        self._path = path

    def __enter__(self) :
        self.add_to_connection(self._bus, self._path)
        return self

    def __exit__(self, exc_type, exc_value, traceback) :
        self.remove_from_connection(self._bus, self._path)
        return True

        


