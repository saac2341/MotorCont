# src/fuentes.py
"""Capa 1 — FUENTES. Único punto que habla con hardware (TCP/Serial/Sim)."""

import socket
import threading
import math

from PySide6.QtCore import QObject, Signal, QTimer

try:
    import serial  # pyserial

    SERIAL_DISPONIBLE = True
except ImportError:
    SERIAL_DISPONIBLE = False


class FuenteBase(QObject):
    """CONTRATO. Todo lo que quiera ser fuente debe heredar de aquí."""

    datos_recibidos = Signal(str)
    estado_conexion = Signal(bool, str)  # (activa?, mensaje)

    @property
    def activa(self) -> bool:
        raise NotImplementedError

    def conectar(self, **kwargs):
        raise NotImplementedError

    def desconectar(self):
        raise NotImplementedError

    def enviar(self, comando: str):
        raise NotImplementedError


# ─────────────────────────────────────────────────────────────────────
class FuenteTCP(FuenteBase):
    """Lee de un socket TCP en un hilo aparte."""

    def __init__(self, ip="192.168.4.1", puerto=5000):
        super().__init__()
        self.ip = ip
        self.puerto = puerto
        self._sock = None
        self._activo = False

    @property
    def activa(self):
        return self._activo

    def conectar(self, **kw):
        if "ip" in kw:
            self.ip = kw["ip"]
        if "puerto" in kw:
            self.puerto = kw["puerto"]
        threading.Thread(target=self._hilo_conectar, daemon=True).start()

    def _hilo_conectar(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5.0)
            sock.connect((self.ip, self.puerto))
            sock.settimeout(None)
            self._sock = sock
            self._activo = True
            self.estado_conexion.emit(True, f"TCP {self.ip}:{self.puerto}")
            self._hilo_leer()
        except Exception as e:
            self._activo = False
            self._sock = None
            self.estado_conexion.emit(False, f"Error TCP: {e}")

    def _hilo_leer(self):
        buffer = ""
        while self._activo and self._sock:
            try:
                data = self._sock.recv(1024)
                if not data:
                    break
                buffer += data.decode("utf-8", errors="ignore")
                while "\n" in buffer:
                    linea, buffer = buffer.split("\n", 1)
                    if linea.strip():
                        self.datos_recibidos.emit(linea.strip())
            except Exception as e:
                self.estado_conexion.emit(False, f"Error recepción: {e}")
                break
        self._finalizar()

    def _finalizar(self):
        self._activo = False
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass
            self._sock = None
        self.estado_conexion.emit(False, "TCP desconectado")

    def desconectar(self):
        if not self._activo:
            return
        self._activo = False
        if self._sock:
            try:
                self._sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            try:
                self._sock.close()
            except Exception:
                pass
            self._sock = None

    def enviar(self, comando):
        if not (self._sock and self._activo):
            return
        try:
            self._sock.sendall((comando + "\n").encode("utf-8"))
        except Exception as e:
            self.estado_conexion.emit(False, f"Error envío TCP: {e}")


# ─────────────────────────────────────────────────────────────────────
class FuenteSerial(FuenteBase):
    """Lee de un puerto serial (pyserial)."""

    def __init__(self, puerto="COM3", baud=115200):
        super().__init__()
        self.puerto = puerto
        self.baud = baud
        self._serial = None
        self._activo = False

    @property
    def activa(self):
        return self._activo

    def conectar(self, **kw):
        if "puerto" in kw:
            self.puerto = kw["puerto"]
        if "baud" in kw:
            self.baud = kw["baud"]
        if not SERIAL_DISPONIBLE:
            self.estado_conexion.emit(False, "pyserial no instalado")
            return
        threading.Thread(target=self._hilo, daemon=True).start()

    def _hilo(self):
        try:
            self._serial = serial.Serial(self.puerto, self.baud, timeout=1)
            self._activo = True
            self.estado_conexion.emit(True, f"Serial {self.puerto}@{self.baud}")
            while self._activo:
                linea = self._serial.readline().decode("utf-8", errors="ignore").strip()
                if linea:
                    self.datos_recibidos.emit(linea)
        except Exception as e:
            self.estado_conexion.emit(False, f"Error serial: {e}")
        finally:
            self._activo = False
            if self._serial and self._serial.is_open:
                try:
                    self._serial.close()
                except Exception:
                    pass
            self.estado_conexion.emit(False, "Serial desconectado")

    def desconectar(self):
        self._activo = False
        if self._serial and self._serial.is_open:
            try:
                self._serial.close()
            except Exception:
                pass

    def enviar(self, comando):
        if self._serial and self._serial.is_open:
            try:
                self._serial.write((comando + "\n").encode("utf-8"))
            except Exception as e:
                self.estado_conexion.emit(False, f"Error envío serial: {e}")


# ─────────────────────────────────────────────────────────────────────
class FuenteSimulada(FuenteBase):
    """Genera una onda senoidal cada `intervalo_ms`. Para probar sin hardware."""

    def __init__(self, intervalo_ms=200):
        super().__init__()
        self._intervalo = intervalo_ms
        self._timer = None
        self._i = 0
        self._activo = False

    @property
    def activa(self):
        return self._activo

    def conectar(self, **kw):
        if "intervalo_ms" in kw:
            self._intervalo = kw["intervalo_ms"]
        self._timer = QTimer()
        self._timer.timeout.connect(self._tick)
        self._timer.start(self._intervalo)
        self._activo = True
        self.estado_conexion.emit(True, "Simulador activo")

    def _tick(self):
        self._i += 1
        valor = math.sin(self._i * 0.1) * 100.0
        self.datos_recibidos.emit(f"{valor:.2f}")

    def desconectar(self):
        if self._timer:
            self._timer.stop()
            self._timer = None
        self._activo = False
        self.estado_conexion.emit(False, "Simulador detenido")

    def enviar(self, comando):
        print(f"[SIM] comando recibido: {comando}")
