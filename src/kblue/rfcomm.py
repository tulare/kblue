# -*- encoding: utf8 -*-

import logging
import re
import socket
import subprocess

__all__ = [ 'RFComm' ]

class RFCommNotConnected(BaseException) :
    pass

class RFCommError(BaseException) :
    pass

class RFComm :

    def __init__(self, bdaddr, port, timeout=5, encoding='utf-8') :
        self.logger = logging.getLogger(self.__class__.__name__)

        self._sock = None
        self.bdaddr = bdaddr
        self.port = port
        self.timeout = timeout
        self.encoding = encoding

    def __enter__(self) :
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback) :
        self.close()
        return True

    @property
    def bdaddr(self) :
        return self._bdaddr

    @bdaddr.setter
    def bdaddr(self, bdaddr) :
        self._bdaddr = bdaddr

    @property
    def port(self) :
        return self._port

    @port.setter
    def port(self, port) :
        self._port = port

    @property
    def timeout(self) :
        return self._timeout

    @timeout.setter
    def timeout(self, timeout) :
        self._timeout = timeout
        if self.connected :
            self._sock.settimeout(self._timeout)

    @property
    def encoding(self) :
        return self._encoding

    @encoding.setter
    def encoding(self, encoding) :
        self._encoding = encoding

    @property
    def connected(self) :
        return self._sock is not None

    def connect(self) :
        if not self.connected :
            self._create_socket()
            self.logger.debug('connect to {} port={}'.format(self._bdaddr, self._port))
            self._sock.connect((self._bdaddr, self._port))
            self.logger.debug('connected')
            
    def close(self) :
        if self.connected :
            self.logger.debug('close socket')
            self._sock.close()
        self._sock = None

    def recv(self, text=False) :
        if not self.connected :
            raise RFCommNotConnected()
        try :
            data = self._sock.recv(1024)
            self.logger.debug('receive {} bytes, text={}'.format(len(data), text))
            if text :
                return data.decode(self._encoding)
            return data
        except (ConnectionResetError, ConnectionAbortedError) as e :
            self.logger.error('{}'.format(e))
            self.close()
            raise RFCommError(e)
        except socket.timeout as e :
            self.logger.error('{}'.format(e))
            raise RFCommError(e)
        except BlockingIOError as e :
            self.logger.error('{}'.format(e))
            raise RFCommError(e)
            
    def send(self, data) :
        if not self.connected :
            raise RFCommNotConnected()
        try :
            if isinstance(data, str) :
                data = data.encode(self._encoding)
            self.logger.debug('send {} bytes : {}'.format(len(data), data))
            return self._sock.send(data)
        except (ConnectionResetError, ConnectionAbortedError) as e :
            self.logger.error('{}'.format(e))
            self.close()
            raise RFCommError(e)
        except socket.timeout as e :
            self.logger.error('{}'.format(e))
            raise RFCommError('timeout')

    @property
    def services(self) :
        command = [ 'sdptool', 'browse', '--l2cap', self.bdaddr ]
        output = subprocess.check_output(command, universal_newlines=True)
        service = None
        services = {}
        for line in output.splitlines() :
            m = re.search('Service Name:\s+(.+)', line)
            if m :
                service = m.group(1)
            m = re.search('Channel:\s+([0-9]+)', line)
            if m and service :
                services[service] = int(m.group(1))
        return services
                                        
    def _create_socket(self) :
        self._sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self._sock.settimeout(self._timeout)
        self.logger.debug('create {}'.format(self._sock))

    def send_to_gateway(self, text=False) :
        self.timeout = 5
        self.close()
        self.connect()
        self.timeout = 1
        self.send(b'AT+BRSF=023\r')
        print(self.recv(text))
        print(self.recv(text))
        self.send(b'AT+CIND=?\r')
        print(self.recv(text))
        print(self.recv(text))
        self.send(b'AT+CIND?\r')
        print(self.recv(text))
        print(self.recv(text))
        self.send(b'AT+CMER=3,0,0,1\r')
        print(self.recv(text))
        self.send(b'AT+CHLD=?\r')
        print(self.recv(text))
        print(self.recv(text))
        self.send(b'AT+CMEE=1\r')
        print(self.recv(text))
        self.send(b'AT+CLIP=1\r')
        print(self.recv(text))
        self.send(b'AT+CCWA=1\r')
        print(self.recv(text))
        self.send(b'AT+NREC=0\r')
        print(self.recv(text))
        self.send(b'AT+VGS=15\r')
        print(self.recv(text))
        self.send(b'AT+VGM=15\r')
        print(self.recv(text))
        self.send(b'AT+XAPL=ABCD-1234-0100,10\r')
        print(self.recv(text))
        self.send(b'AT+IPHONEACCEV=1,1,4\r')
        print(self.recv(text))
        

    def recv_from_gateway(self, text=False) :
        self.timeout = 5
        self.close()
        self.connect()
        self.timeout = 1
        print(self.recv(text))
        self.send(b'\r\n+BRSF: 871\r\n')
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(
            b'\r\n+CIND: ("call",(0,1)),("callsetup",(0-3)),("service",(0-1)),("signal",(0-5)),("roam",(0,1)),("battchg",(0-5)),("callheld",(0-2))\r\n'
        )
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\n+CIND: 0,0,0,0,0,1,0\r\n')
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\n+CHLD: (0,1,2,3)\r\n')
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')
        print(self.recv(text))
        self.send(b'\r\nOK\r\n')

"""
> b'AT+BRSF=023\r'
< b'\r\n+BRSF: 871\r\n'
< b'\r\nOK\r\n'

> b'AT+CIND=?\r'
< b'\r\n+CIND: ("call",(0,1)),("callsetup",(0-3)),("service",(0-1)),("signal",(0-5)),("roam",(0,1)),("battchg",(0-5)),("callheld",(0-2))\r\n'
< b'\r\nOK\r\n'

> b'AT+CIND?\r'
< b'\r\n+CIND: 0,0,0,0,0,1,0\r\n'
< b'\r\nOK\r\n'

> b'AT+CMER=3,0,0,1\r'
< b'\r\nOK\r\n'

> b'AT+CHLD=?\r'
< b'\r\n+CHLD: (0,1,2,3)\r\n'
< b'\r\nOK\r\n'

> b'AT+CMEE=1\r'
< b'\r\nOK\r\n'

> b'AT+CLIP=1\r'
< b'\r\nOK\r\n'

> b'AT+CCWA=1\r'
< b'\r\nOK\r\n'

> b'AT+NREC=0\r'
< b'\r\nOK\r\n'

> b'AT+VGS=15\r'
< b'\r\nOK\r\n'

> b'AT+VGM=15\r'
< b'\r\nOK\r\n'

> b'AT+XAPL=ABCD-1234-0100,10\r'
< b'\r\nOK\r\n'

> b'AT+IPHONEACCEV=1,1,4\r'
< b'\r\nOK\r\n'
"""
