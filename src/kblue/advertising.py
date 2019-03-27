# -*- encoding: utf-8 -*-

import re
import struct
import binascii
from .helpers import adv_name
from .btmgexp import BtMgmt

__all__ = [ 'BLEAdvertiser' ]

# ------------------------------------------------------------------------------
# --- BLEAdvertiser ------------------------------------------------------------
# ------------------------------------------------------------------------------

class BLEAdvertiser :

    def __init__(self) :
        self._bt = BtMgmt(sudo=True)

    def count(self) :
        res = self._bt._sendcmd('advinfo')
        motif = re.compile('Instances list with ([0-9]+) item')
        m = re.search(motif, res)
        return int(m.groups()[-1])
        
    def add_connectable(self, name, instance=1) :
        return self._bt._sendcmd('add-adv', '-c', '-g', '-s', adv_name(name).hex(), instance)

    def add_ibeacon(self, uuid, major, minor, tx_power, instance=1) :
        """
        1aff4c0002158deefbb9f7384297804096668bb4428100012258c5
        1aff4c00 -> manuf : apple inc. iBeacon
                0215 -> header
                    8deefbb9f7384297804096668bb44281 -> uuid
                                                    0001 -> major
                                                        2258 -> minor
                                                            c5 -> tx
        """
        manuf = '1aff4c00'
        header = '0215'
        adv_uuid = uuid.hex
        adv_major = binascii.hexlify(struct.pack('>H', major)).decode()
        adv_minor = binascii.hexlify(struct.pack('>H', minor)).decode()
        adv_tx_power = binascii.hexlify(struct.pack('b', tx_power)).decode()
        data = manuf + header + adv_uuid + adv_major + adv_minor + adv_tx_power

        return self._bt._sendcmd('add-adv', '-g', '-d', data, instance)

    def remove(self, instance=1) :
        return self._bt._sendcmd('rm-adv', instance)

    def clear_all(self) :
        return self._bt._sendcmd('clr-adv')
