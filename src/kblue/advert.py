# -*- encoding: utf-8 -*-

import time
import struct
from .helpers import unpack_uuid
from .vendors import (
    getCompany, getAppearance, getServiceUUID16
)


__all__ = [ 'BLEAdvert' ]

APPLE_IBEACON_FORMAT = """
    UUID    : {}
    Major   : {} ({})
    Minor   : {} ({})
    TxPower : {} dBm"""

# ------------------------------------------------------------------------------        
class AdvData :

    def __init__(self, adtype, advdata) :
        self._adtype = adtype
        self._advdata = advdata

    def __str__(self) :
        return '[{}] {} : {}'.format(
            self.adtype,
            self.classname,
            self.advdata
        )

    @property
    def classname(self) :
        return self.__class__.__name__

    @property
    def adtype(self) :
        return '0x{:02x}'.format(self._adtype)

    @property
    def advdata(self) :
        return self._advdata.hex() 

# ------------------------------------------------------------------------------
class AdvFlags(AdvData) :

    def __init__(self, adtype, advdata) :
        super().__init__(adtype, advdata)
        self._flags, = struct.unpack('B', self._advdata)

    def __str__(self) :
        return '[{}] {} : {}'.format(
            self.adtype,
            self.classname,
            self.flags
        )

    @property
    def flags(self) :
        return '0b{:08b}'.format(self._flags)

# ------------------------------------------------------------------------------
class AdvName(AdvData) :

    def __init__(self, adtype, advdata) :
        super().__init__(adtype, advdata)
        self._name = self._advdata

    def __str__(self) :
        return '[{}] {} : {}'.format(
            self.adtype,
            self.classname,
            self.name
        )

    @property
    def name(self) :
        return self._name
        
# ------------------------------------------------------------------------------
class AdvListUuid(AdvData) :

    def __init__(self, adtype, advdata, uuidlen) :
        super().__init__(adtype, advdata)
        self._uuidlen = uuidlen
        self._uuids = [
                self._advdata[i:i+uuidlen]
                for i in range(0, len(self._advdata), uuidlen)
        ]

    def __str__(self) :
        return '[{}] {} : {}'.format(
            self.adtype,
            self.classname,
            self.uuids
        )        

    @property
    def uuids(self) :
        return ', '.join(unpack_uuid(u) for u in self._uuids)

# ------------------------------------------------------------------------------
class AdvListUuid16(AdvListUuid) :

    def __init__(self, adtype, advdata) :
        super().__init__(adtype, advdata, 2)

    @property
    def uuids(self) :
        return ', '.join(
            '{} ({})'.format(
                getServiceUUID16(struct.unpack('<H', u)[0]),
                unpack_uuid(u)
            )
            for u in self._uuids
        )

# ------------------------------------------------------------------------------
class ProximityHelper :

    @staticmethod
    def _txFormula(A, B, C, r, t) :
        return A * ( (r/t) ** B ) + C

    @staticmethod
    def LogTX(rssi, rssiTX, n_PathLossExp=2) :
        return 10.0 ** ( (rssi-rssiTX) / (-10*n_PathLossExp) )

    @staticmethod
    def OldBconTX(rssi, rssiTX) :
        return ProximityHelper._txFormula(0.89976, 7.7095, 0.111, rssi, rssiTX)

    @staticmethod
    def NewBconTX(rssi, rssiTX) :
        return ProximityHelper._txFormula(0.42093, 6.9476, 0.54992, rssi, rssiTX)


class BLEAdvert :

    # ============================================================================
    # ===( Exceptions )===========================================================
    # ============================================================================
    class ErrorPacketLen(BaseException) :
        pass

    class ErrorAdvDataLen(BaseException) :
        pass

    class UnknownVendor(BaseException) :
        pass

    class InvalidAppleIBeacon(BaseException) :
        pass

    class InvalidAppleService(BaseException) :
        pass

    # ============================================================================
    # ===( Constants )============================================================
    # ============================================================================

    DATA_TYPE_FLAGS                 = 0x01
    DATA_TYPE_INCOMP_16BITS_UUIDS   = 0x02
    DATA_TYPE_COMP_16BITS_UUIDS     = 0x03
    DATA_TYPE_INCOMP_32BITS_UUIDS   = 0x04
    DATA_TYPE_COMP_32BITS_UUIDS     = 0x05
    DATA_TYPE_INCOMP_128BITS_UUIDS  = 0x06
    DATA_TYPE_COMP_128BITS_UUIDS    = 0x07
    DATA_TYPE_SHORT_NAME            = 0x08
    DATA_TYPE_COMPLETE_NAME         = 0x09
    DATA_TYPE_TX_POWER_LEVEL        = 0x0A
    DATA_TYPE_DEVICE_CLASS          = 0x0B
    DATA_TYPE_SMP_PAIR_HASH_C       = 0x0C
    DATA_TYPE_SMP_PAIR_HASH_C192    = 0x0D
    DATA_TYPE_SMP_PAIR_RAND_R       = 0x0E
    DATA_TYPE_SMP_PAIR_RAND_R192    = 0x0F
    DATA_TYPE_DEVICE_ID             = 0x10
    DATA_TYPE_SECU_MNGR_TK_VAL      = 0x11
    DATA_TYPE_SECU_MNGR_OOB_FLAGS   = 0x12
    DATA_TYPE_SLAVE_CONN_INT_RNG    = 0x13
    DATA_TYPE_16BITS_SVC_SOL_UUIDS  = 0x14
    DATA_TYPE_128BITS_SVC_SOL_UUIDS = 0x15
    DATA_TYPE_SVC_DATA              = 0x16
    DATA_TYPE_PUB_TARGET_ADDR       = 0x17
    DATA_TYPE_RAND_TARGET_ADDR      = 0x18
    DATA_TYPE_APPEARANCE            = 0x19
    DATA_TYPE_ADV_INT               = 0x1A    
    DATA_TYPE_LE_BLT_DEVICE_ADDR    = 0x1B
    DATA_TYPE_LE_ROLE               = 0x1C
    DATA_TYPE_SMP_PAIR_HASH_C256    = 0x1D
    DATA_TYPE_SMP_PAIR_RAND_R256    = 0x1E
    DATA_TYPE_32BITS_SVC_SOL_UUIDS  = 0x1F
    DATA_TYPE_SVC_DATA_32BITS_UUID  = 0x20
    DATA_TYPE_SVC_DATA_128BITS_UUID = 0x21
    DATA_TYPE_LE_SECU_CONN_CONF_VAL = 0x22
    DATA_TYPE_LE_SECU_CONN_RAND_VAL = 0x23
    DATA_TYPE_URI                   = 0x24
    DATA_TYPE_INDOOR_POS            = 0x25
    DATA_TYPE_TRANS_DISCOV_DATA     = 0x26
    DATA_TYPE_LE_SUPPORT_FEAT       = 0x27
    DATA_TYPE_CHAN_MAP_UPD_INDIC    = 0x28
    DATA_TYPE_PB_ADV                = 0x29
    DATA_TYPE_MESH_MSG              = 0x2A
    DATA_TYPE_MESH_BEACON           = 0x2B
    DATA_TYPE_3D_INFO_DATA          = 0x3D
    DATA_TYPE_MANUFACTURER_DATA     = 0xFF

    APPLE_TYPE_IBEACON              = 0x02
    APPLE_TYPE_AIRDROP              = 0x05
    APPLE_TYPE_AIRPODS              = 0x07
    APPLE_TYPE_AIRPLAY_DEST         = 0x09
    APPLE_TYPE_AIRPLAY_SRC          = 0x0A
    APPLE_TYPE_HANDOFF              = 0x0C
    APPLE_TYPE_NEARBY               = 0x10
    
    # ============================================================================
    # ===( Constructor )==========================================================
    # ============================================================================
    
    def __init__(self, packet, timestamp=None) :
        self._packet = packet
        self._timestamp = timestamp
        self._extract_pdu()
        self._extract_adv_data()
        self._decode_adv_data()
        self._parse_manufacturer_data()
        self._parse_service_data()

    def _extract_pdu(self) :
        reserv0, pkt_len, reserv1 = struct.unpack_from('>HBH', self._packet)
        if pkt_len + 3 != len(self._packet) :
            raise self.ErrorPacketLen('bad packet length')
        self._pdu = {
            'header' : self._packet[5:7],
            'bdaddr' : self._packet[7:13],
            'datalen' : self._packet[13],
            'advdata' : self._packet[14:-1],
            'rssi' : self._packet[-1:]
        }

    def _extract_adv_data(self) :
        if self._pdu['datalen'] != len(self._pdu['advdata']) :
            raise self.ErrorAdvDataLen('bad adv data size')
        self._advdata = {}
        offset = 0
        while offset < self._pdu['datalen'] :
            adlen, adtype = struct.unpack_from('BB', self._pdu['advdata'], offset)
            self._advdata[adtype], = struct.unpack_from(
                '{}s'.format(adlen - 1),
                self._pdu['advdata'],
                offset + 2
            )
            offset += adlen + 1

    def _decode_adv_data(self):
        self._advobj = []
        for adtype, advdata in self._advdata.items() :
            if adtype   == self.DATA_TYPE_FLAGS :
                obj = self.Flags(adtype, advdata)
            elif adtype == self.DATA_TYPE_INCOMP_16BITS_UUIDS :
                obj = self.IncompleteListUuid16(adtype, advdata)
            elif adtype == self.DATA_TYPE_COMP_16BITS_UUIDS :
                obj = self.CompleteListUuid16(adtype, advdata)
            elif adtype == self.DATA_TYPE_INCOMP_32BITS_UUIDS :
                obj = self.IncompleteListUuid32(adtype, advdata)
            elif adtype == self.DATA_TYPE_COMP_32BITS_UUIDS :
                obj = self.CompleteListUuid(adtype, advdata)
            elif adtype == self.DATA_TYPE_INCOMP_128BITS_UUIDS :
                obj = self.IncompleteListUuid128(adtype, advdata)
            elif adtype == self.DATA_TYPE_COMP_128BITS_UUIDS :
                obj = self.CompleteListUuid128(adtype, advdata)
            elif adtype == self.DATA_TYPE_SHORT_NAME :
                obj = self.ShortName(adtype, advdata)
            elif adtype == self.DATA_TYPE_COMPLETE_NAME :
                obj = self.CompleteName(adtype, advdata)
            elif adtype == self.DATA_TYPE_TX_POWER_LEVEL :
                obj = self.TxPowerLevel(adtype, advdata)
            elif adtype == self.DATA_TYPE_SVC_DATA :
                obj = self.ServiceData(adtype, advdata)
            elif adtype == self.DATA_TYPE_APPEARANCE :
                obj = self.Appearance(adtype, advdata)
            elif adtype == self.DATA_TYPE_MANUFACTURER_DATA :
                obj = self.ManufacturerData(adtype, advdata)
            else :
                obj = self.UnknownData(adtype, advdata)
            self._advobj.append(obj)

    def _parse_manufacturer_data(self) :
        for obj in self._advobj :
            if type(obj) == self.ManufacturerData :
                if obj._code == '0x004c' : # APPLE
                    if obj._vendordata[0] == self.APPLE_TYPE_IBEACON :
                        try :
                            newobj = self.AppleIBeacon(obj._adtype, obj._advdata)
                            self._advobj.append(newobj)
                        except self.InvalidAppleIBeacon :
                            pass
                    else :
                        try :
                            newobj = self.AppleService(obj._adtype, obj._advdata)
                            self._advobj.append(newobj)
                        except self.InvalidAppleService :
                            pass

    def _parse_service_data(self) :
        for obj in self._advobj :
            if type(obj) == self.ServiceData :
                pass
            
    # ============================================================================
    # ===( Properties )===========================================================
    # ============================================================================

    @property
    def timestamp(self) :
        return self._timestamp

    @property
    def bdaddr(self) :
        return ':'.join(
            '{:02X}'.format(b) for b in bytes(reversed(self._pdu['bdaddr']))
        )

    @property
    def header(self) :
        header = self._pdu['header']
        pdu_type_bin = '{:04b}'.format(header[0] & 0b1111)
        pdu_rfu1 = (header[0] & 0b110000) >> 4
        pdu_txad = (header[0] & 0b1000000) >> 6
        pdu_rxad = (header[0] & 0b10000000) >> 7
        pdu_len  =  header[1] & 0b111111
        pdu_rfu2 =  header[1] >> 6        
        if pdu_type_bin == '0000' :
            pdu_type = 'ADV_IND'
        elif pdu_type_bin == '0001' :
            pdu_type = 'ADV_DIRECT_IND'
        elif pdu_type_bin == '0010' :
            pdu_type = 'ADV_NONCONN_IND'
        elif pdu_type_bin == '0011' :
            pdu_type = 'SCAN_REQ'
        elif pdu_type_bin == '0100' :
            pdu_type = 'SCAN_RSP'
        elif pdu_type_bin == '0101' :
            pdu_type = 'CONNECT_REQ'
        elif pdu_type_bin == '0110' :
            pdu_type = 'ADV_SCAN_IND'
        else :
            pdu_type = 'ADV_UNKNOWN'
            
        return pdu_type, pdu_txad, pdu_rxad, pdu_len
    
    @property
    def rssi(self) :
        return struct.unpack('b', self._pdu['rssi'])[0]

    # ============================================================================
    # ===( Filters )==============================================================
    # ============================================================================

    def matchName(self, motif) :
        motif_bin = motif.encode()
        for obj in self._advobj :
            if isinstance(obj, AdvName) :
                if motif_bin in obj.name :
                    return True
        return False

    def isAppleIBeacon(self) :
        for obj in self._advobj :
            if isinstance(obj, self.AppleIBeacon) :
                return True
        return False

    def matchServiceUUID(self, motif) :
        for obj in self._advobj :
            if isinstance(obj, self.ServiceData) :
                if motif in obj.uuid :
                    return True
                if motif in obj.member :
                    return True
            if isinstance(obj, AdvListUuid) :
                if motif in obj.uuids :
                    return True
        return False

    def matchAppleService(self, motif) :
        for obj in self._advobj :
            if isinstance(obj, self.AppleService) :
                if motif in obj.service :
                    return True
        return False

    def matchIBeaconUUID(self, motif) :
        for obj in self._advobj :
            if isinstance(obj, self.AppleIBeacon) :
                if motif in obj.uuid :
                    return True
        return False

    def matchCompany(self, motif) :
        for obj in self._advobj :
            if isinstance(obj, self.ManufacturerData) :
                if motif in obj.company :
                    return True
        return False
        

    # ============================================================================
    # ===( Introspect )===========================================================
    # ============================================================================

    def dump_data(self, adtype, sep='') :
        advdata = self._advdata.get(adtype, b'')
        return sep.join('{:02X}'.format(o) for o in advdata)

    def print(self) :
        timestamp = time.strftime(
            '%d/%m/%Y %H:%M:%S', time.localtime(self.timestamp)
        )
        print('-' * 80)
        print('BDADDR : {}'.format(self.bdaddr))
        print('HEADER : {}'.format(self.header))
        print('TIME   : {} [{:.03f}]'.format(timestamp, self.timestamp))
        print('RSSI   : {} dBm'.format(self.rssi))
        for obj in self._advobj :
            print(obj)
            if isinstance(obj, self.AppleIBeacon) :
                print(
                    'Proximity : LogTx={:0.1f}m OldBconTX={:0.1f}m NewBconTx={:0.1f}m'.format(
                        obj.GetProximityByLogTX(self.rssi),
                        obj.GetProximityByOldBconTX(self.rssi),
                        obj.GetProximityByNewBconTX(self.rssi)
                    )
                )
        print()

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================

    class UnknownData(AdvData) :
        pass

    class Flags(AdvFlags) :
        pass

    class IncompleteListUuid16(AdvListUuid16) :
        pass
    
    class CompleteListUuid16(AdvListUuid16) :
        pass
    
    class IncompleteListUuid32(AdvListUuid) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata, 4)

    class CompleteListUuid32(AdvListUuid) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata, 4)

    class IncompleteListUuid128(AdvListUuid) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata, 16)

    class CompleteListUuid128(AdvListUuid) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata, 16)

    class ShortName(AdvName) :
        pass

    class CompleteName(AdvName) :
        pass

    class TxPowerLevel(AdvName) :
        def __str__(self) :
            return '{} : {} dBm'.format(
                self.__class__.__name__,
                struct.unpack('b', self._advdata)[0]
            )   

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================

    class Appearance(AdvData) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata)
            app, = struct.unpack('<H', self._advdata)
            self._categ = app >> 6
            self._subcateg = app & 0b111111

        def __str__(self) :
            return '[{}] {} : {} ({}, {})'.format(
                self.adtype,
                self.classname,
                self.desc,
                self.categ,
                self.subcateg
            )

        @property
        def desc(self) :
            return getAppearance(self.categ, self.subcateg)

        @property
        def categ(self) :
            return self._categ

        @property
        def subcateg(self) :
            return self._subcateg

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================
    
    class ServiceData(AdvData) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata)
            self._uuid = self._advdata[:2]
            self._member = getServiceUUID16(
                struct.unpack('<H', self._uuid)[0]
            )
            self._data = self._advdata[2:]

        def __str__(self) :
            return '[{}] {} {} ({}) : {}'.format(
                self.adtype,
                self.classname,
                self.member,
                self.uuid,
                self.data
            )

        @property
        def uuid(self) :
            return unpack_uuid(self._uuid)

        @property
        def member(self):
            return self._member
            
        @property
        def data(self) :
            return self._data.hex()

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================

    class ManufacturerData(AdvData) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata)
            self._code, self._company = getCompany(
                struct.unpack('<H', self._advdata[:2])[0]
            )
            self._vendordata = self._advdata[2:]

        def __str__(self) :
            return '[{}] {} ({}) : {}'.format(
                self.adtype,
                self.company,
                self.code,
                self.vendordata
            )

        @property
        def code(self) :
            return self._code

        @property
        def company(self) :
            return self._company
        
        @property
        def vendordata(self) :
            return self._vendordata.hex()

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================
                
    class AppleIBeacon(ManufacturerData) :
        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata)
            self._sig, self._len = self._vendordata[:2]
            self._uuid = self._vendordata[2:18]
            self._major = self._vendordata[18:20]
            self._minor = self._vendordata[20:22]
            self._txpower = self._vendordata[-1:]
            if self._sig != 0x02 :
                raise BLEAdvert.InvalidAppleIBeacon('invalid apple ibeacon')

        @property
        def sig(self) :
            return '0x{:02x}'.format(self._sig)

        @property
        def uuid(self) :
            return unpack_uuid(self._uuid, bigendian=True)

        @property
        def major(self) :
            return struct.unpack('>H', self._major)[0]

        @property
        def minor(self) :
            return struct.unpack('>H', self._minor)[0]

        @property
        def txpower(self) :
            return struct.unpack('b', self._txpower)[0]

        def GetProximityByLogTX(self, rssi, n_PathLossExp=2) :
            return ProximityHelper.LogTX(rssi, self.txpower, n_PathLossExp)

        def GetProximityByOldBconTX(self, rssi) :
            return ProximityHelper.OldBconTX(rssi, self.txpower)

        def GetProximityByNewBconTX(self, rssi) :
            return ProximityHelper.NewBconTX(rssi, self.txpower)

        def __str__(self) :
            return ('[{}] {} ({}) :' + APPLE_IBEACON_FORMAT).format(
                self.adtype,
                self.classname,
                self.sig,
                self.uuid,
                self.major, hex(self.major),
                self.minor, hex(self.minor),
                self.txpower
            )

    # ============================================================================
    # ===( Inner Classes )========================================================
    # ============================================================================

    class AppleService(ManufacturerData) :

        def __init__(self, adtype, advdata) :
            super().__init__(adtype, advdata)
            self._sig, self._len = self._vendordata[:2]
            self._data = self._vendordata[2:]

        @property
        def sig(self) :
            return '0x{:02x}'.format(self._sig)

        @property
        def service(self) :
            name = 'Unknown'
            if   self._sig == BLEAdvert.APPLE_TYPE_AIRDROP :
                name = 'AirDrop'
            elif self._sig == BLEAdvert.APPLE_TYPE_AIRPODS :
                name = 'AirPods'
            elif self._sig == BLEAdvert.APPLE_TYPE_AIRPLAY_DEST :
                name = 'AirPlay Destination'
            elif self._sig == BLEAdvert.APPLE_TYPE_AIRPLAY_SRC :
                name = 'AirPlay Source'
            elif self._sig == BLEAdvert.APPLE_TYPE_HANDOFF :
                name = 'HandOff'
            elif self._sig == BLEAdvert.APPLE_TYPE_NEARBY :
                name = 'Nearby'
            return name

        @property
        def data(self) :
            return self._data.hex()

        def __str__(self) :
            return '[{}] {} {} ({}) : {}'.format(
                self.adtype,
                self.classname,
                self.service,
                self.sig,
                self.data
            )
