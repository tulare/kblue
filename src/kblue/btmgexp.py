# -*- encoding: utf-8 -*-

import subprocess

# ------------------------------------------------------------------------------
# --- Class BtMgmt -------------------------------------------------------------
# ------------------------------------------------------------------------------

class BtMgmt :

    def __init__(self, device_idx=0, sudo=False, echo=False) :
        self._device_idx = device_idx
        self._sudo = sudo
        self._echo = echo

    @property
    def sudo(self) :
        return self._sudo

    @sudo.setter
    def sudo(self, sudo) :
        self._sudo = sudo

    @property
    def echo(self) :
        return self._echo

    @echo.setter
    def echo(self, echo) :
        self._echo = echo

    def _sendcmd(self, command, *args, timeout=30) :
        command = [
            'btmgmt', '--index', str(self._device_idx),
            command,
            *(str(a) for a in args)
        ]
        if self.sudo :
            command.insert(0, 'sudo')
        if self.echo :
            print(' '.join(command))
        proc = subprocess.Popen(
            command,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines=True
        )
        out, err = proc.communicate(timeout=timeout)
        if proc.returncode != 0 :
            raise OSError(proc.returncode, err)
        return out

    def info(self, timeout=1) :
        return self._sendcmd('info', timeout=timeout)


    def con(self, timeout=2) :
        return self._sendcmd('con', timeout=timeout)

    def conn_info(self, bdaddr, addr_type, timeout=2) :
        """
        conn-info [-t type] <remote address>
        """
        return self._sendcmd('conn-info', '-t', str(addr_type), bdaddr, timeout=timeout)

    def pair(self, bdaddr, addr_type, cap=1, timeout=5) :
        """
        pair [-c cap] [-t type] <remote address>
        """
        return self._sendcmd('pair', '-c', str(cap), '-t', str(addr_type), bdaddr, timeout=timeout)

    def cancelpair(self, bdaddr, addr_type, timeout=2) :
        """
        cancelpair [-t type] <remote address>
        """
        return self._sendcmd('cancelpair', '-t', str(addr_type), bdaddr, timeout=timeout)

    def unpair(self, bdaddr, addr_type, timeout=2) :
        """
        unpair [-t type] <remote address>
        """
        return self._sendcmd('unpair', '-t', str(addr_type), bdaddr, timeout=timeout)
