# -*- encoding: utf-8 -*-

import dbus

from .const import *
from .core import Node

__all__ = [ 'NetworkServer', 'Network' ]

# ------------------------------------------------------------------------------
# --- Class NetworkServer ------------------------------------------------------
# ------------------------------------------------------------------------------

class NetworkServer(Node) :

    INTERFACE = NETWORK_SERVER_INTERFACE

# ------------------------------------------------------------------------------
# --- Class Network ------------------------------------------------------------
# ------------------------------------------------------------------------------

class Network(Node) :

    INTERFACE = NETWORK_INTERFACE

    @property
    def connected(self) :
        return bool(self.Connected)

    @property
    def uuid(self) :
        if self.connected :
            return str(self.UUID)
        
    @property
    def network_interface(self) :
        if self.connected :
            return str(self.Interface) 
        
