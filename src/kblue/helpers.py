# -*- encoding : utf-8 -*-

import struct
from uuid import UUID

# ------------------------------------------------------------------------------
# --- Advertising Misc ---------------------------------------------------------
# ------------------------------------------------------------------------------

def adv_data(adv_type, data) :
    adv_t = struct.pack('B', adv_type)
    if not isinstance(data, bytes) :
        data = data.encode()
    length = struct.pack('B', len(adv_t + data))
    return length + adv_t + data

def adv_name(name, short=False) :
    adv_type = 0x08 if short else 0x09
    return adv_data(adv_type, name)

# ------------------------------------------------------------------------------
# --- Misc UUID 16, 128 --------------------------------------------------------
# ------------------------------------------------------------------------------

def unpack_uuid(data, bigendian=False) :
    """
    data as bytes
    """
    if not bigendian :
        data = bytes(reversed(data))

    if len(data) == 16 : # 128 bits uuid
        return str(UUID(bytes=data))
    else :
        return data.hex()
    
# ------------------------------------------------------------------------------

def pack_uuid(uuid, bigendian=False) :
    """
    uuid as string
    """
    try :
        data = UUID(uuid).bytes
    except ValueError :
        data = bytes.fromhex(uuid)

    if not bigendian :
        data = bytes(reversed(data))

    return data

# ------------------------------------------------------------------------------        

def full_uuid(uuid) :
    if isinstance(uuid, UUID) :
        return uuid
    if isinstance(uuid, str) :
        try :
            return str(UUID(uuid))
        except ValueError :
            pass
        bt_uuid_mask = '0000{}-0000-1000-8000-00805f9b34fb'
    if isinstance(uuid, int) :
        bt_uuid_mask = '0000{:04x}-0000-1000-8000-00805f9b34fb'
    
    return str(UUID(bt_uuid_mask.format(uuid)))

# ------------------------------------------------------------------------------

def short_uuid(uuid128) :
    uuid16 = uuid128[4:8]
    return int(uuid16, 16)

# ------------------------------------------------------------------------------
# --- Misc GATT  ---------------------------------------------------------------
# ------------------------------------------------------------------------------

CHAR_FLAG_BROADCAST = 0b00000001
CHAR_FLAG_READ      = 0b00000010
CHAR_FLAG_WRITEWORP = 0b00000100
CHAR_FLAG_WRITE     = 0b00001000
CHAR_FLAG_NOTIFY    = 0b00010000
CHAR_FLAG_INDICATE  = 0b00100000
CHAR_FLAG_AUTHWRITE = 0b01000000
CHAR_FLAG_EXTENDED  = 0b10000000

def char_properties(flags) :
    prop = ''
    if flags & CHAR_FLAG_EXTENDED :
        prop += 'x'
    else :
        prop += '-'
    if flags & CHAR_FLAG_AUTHWRITE :
        prop += 's'
    else :
        prop += '-'
    if flags & CHAR_FLAG_INDICATE :
        prop += 'i'
    else :
        prop += '-'
    if flags & CHAR_FLAG_NOTIFY :
        prop += 'n'
    else :
        prop += '-'
    if flags & CHAR_FLAG_WRITE :
        prop += 'w'
    else :
        prop += '-'
    if flags & CHAR_FLAG_WRITEWORP :
        prop += 'W'
    else :
        prop += '-'
    if flags & CHAR_FLAG_READ :
        prop += 'r'
    else :
        prop += '-'
    if flags & CHAR_FLAG_BROADCAST :
        prop += 'b'
    else :
        prop += '-'
    return prop
