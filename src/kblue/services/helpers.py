# -*- encoding: utf-8 -*-

import os
import types

__all__ = [
    'dbus_session_bus_address', 'display',
    'build_signal'
]

# ------------------------------------------------------------------------------

def dbus_session_bus_address() :
    return os.environ.get('DBUS_SESSION_BUS_ADDRESS')

# ------------------------------------------------------------------------------

def display() :
    return os.environ.get('DISPLAY')

# ------------------------------------------------------------------------------

def build_signal(name, nargs=0) :
    store = {}
    code = "def signal(self, {}) : pass".format(
        ', '.join('arg'+str(n+1) for n in range(nargs))
    )
    exec(code, {}, store)
    return types.FunctionType(store['signal'].__code__, {}, name)
