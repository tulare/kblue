# -*- encoding: utf-8 -*-

import re
import time

from .btmgexp import BtMgmt
from .core import Device
from .helpers import full_uuid
from .utils import find_adapter, find_devices, find_devices_with_uuid

__all__ = [
    'le_find', 'le_find_service',
    'le_dbus_find', 'le_find_uuid'
]

# ------------------------------------------------------------------------------
# --- Misc ---------------------------------------------------------------------
# ------------------------------------------------------------------------------

def parse_find_response(response) :
    dct = dict()
    motif_dev = re.compile('dev_found: (.+) type (.+) rssi (.+) flags (\S+)')
    motif_name = re.compile('name (.+)')
    addr = ''
    for line in response.splitlines() :
        dev = re.findall(motif_dev, line)
        if dev :
            addr, type_addr, rssi, flags = dev[-1]
            entry = dct.get(addr, {
                'type' : type_addr,
                'name' : None,
                'rssi' : [],
                'flags' : flags
            })
            entry['rssi'].append(rssi)
            dct.update({ addr : entry })
        name = re.findall(motif_name, line)
        if name :
            entry = dct.get(addr)
            entry['name'], = name
    return dct

# ------------------------------------------------------------------------------
# --- LE Discovering -----------------------------------------------------------
# ------------------------------------------------------------------------------

def le_find() :
    """
    sudo btmgmt find -l
    """
    bt = BtMgmt(sudo=True)
    response = bt._sendcmd('find', '-l')
    return parse_find_response(response) 

def le_find_service(uuid=None, rssi=None) :
    """
    sudo btmgmt find-service -u 905efe00-81e9-4796-9b75-b95cf5e30c0b -l
    sudo btmgmt find-service -u fe33 -r -66 -l
    """
    options = []
    if uuid is not None :
        options.append('-u')
        options.append(str(uuid))
    if rssi is not None :
        options.append('-r')
        options.append(int(rssi))        
    bt = BtMgmt(sudo=True)
    response = bt._sendcmd('find-service', *options, '-l')
    return parse_find_response(response)


# ------------------------------------------------------------------------------
# --- Discovering via DBUS -----------------------------------------------------
# ------------------------------------------------------------------------------

def le_dbus_find(duration=4) :
    adapter = find_adapter()
    adapter.StartDiscovery()
    time.sleep(duration)
    devices = find_devices()
    adapter.StopDiscovery()
    return [
        Device(device)
        for device in devices
    ]
    
def le_dbus_find_uuid(uuid, duration=4) :
    uuid128 = full_uuid(uuid)
    adapter = find_adapter()
    adapter.StartDiscovery()
    time.sleep(duration)
    devices = find_devices_with_uuid(uuid128)
    adapter.StopDiscovery()
    return [
        Device(device)
        for device in devices
    ]
