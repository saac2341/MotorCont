"""Puentes de comunicación con el hardware, unico punto que habla con el hardware y abstrae la lógica de la interfaz de usuario."""

import socket
import threading
import math 

from PyQt6.QtCore import QObject, Signal, QTimer

try:
    import serial # instalar pyserial para su uso
    SERIAL_DISPONIBLE = True
except ImportError:
    SERIAL_DISPONIBLE = False

"""Definicion de la clase(contrato) de la interfaz de comunicación con el hardware, que debe ser implementada por cada tipo de hardware."""
class FuenteBase(QObject):
    datos_recibidos = Signal(str)  # Señal para transmitir datos recibidos a otras interfaces
    estado_conexion = Signal(bool, str)  # Señal para transmitir el estado de la conexión a otras interfaces

    @property
    def activa(self) -> bool:
        """Indica si la fuente de datos está activa y conectada."""
        raise NotImplementedError
    def conectar(self, **kwargs):
        """Establece la conexión con la fuente de datos."""
        raise NotImplementedError
    def desconectar(self):
        """Cierra la conexión con la fuente de datos."""
        raise NotImplementedError
    def enviar_datos(self, datos: str):
        """Envía datos a la fuente de datos."""
        raise NotImplementedError

class FuenteTCP(FuenteBase):
    """Implementación de la fuente de datos mediante conexión TCP/IP."""

    def __init__(self, ip = "127.0.0.1", puerto = 5000):
        super().__init__()
        self.ip = ip
        self.puerto = puerto
        self.socket = None
        self._activa = False

    @property
    def activa(self) -> bool:
        return self._activa

    def conectar(self, host: str, port: int):
        """Establece la conexión TCP con el host y puerto especificados."""
        if self._activa:
            return  # Ya está conectada

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            self._activa = True
            self.estado_conexion.emit(True, "Conectado a {}:{}".format(host, port))
            # Iniciar hilo de lectura de datos
            self._hilo_lectura = threading.Thread(target=self._leer_datos, daemon=True)
            self._hilo_lectura.start()
        except Exception as e:
            self.estado_conexion.emit(False, "Error al conectar: {}".format(e))

    def desconectar(self):
        """Cierra la conexión TCP."""
        if not self._activa:
            return  # No está conectada

        try:
            if self.socket:
                self.socket.close()
                self.socket = None
            self._activa = False
            self.estado_conexion.emit(False, "Desconectado")
        except Exception as e:
            self.estado_conexion.emit(False, "Error al desconectar: {}".format(e))

    def enviar_datos(self, datos: str):
        """Envía datos a través del socket TCP."""
        if not self._activa or not self.socket:
            return  # No está conectada

        try:
            self.socket.sendall(datos.encode('utf-8'))
        except Exception as e:
            self.estado_conexion.emit(False, "Error al enviar datos: {}".format(e))