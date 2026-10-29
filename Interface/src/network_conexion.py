# src/network_worker.py
"""Librería encargada de realizar las conexiones con la ESP32 a través de Wi-Fi."""

import socket
import threading
import time
from PySide6.QtCore import QObject, Signal, Slot
from scipy import signal

class NetworkConexion(QObject):
    """Clase encargada de la conexión con la ESP32 a través de Wi-Fi adaptada a PySide6."""

    # Señales para notificar a la interfaz gráfica sin congelar la ventana
    datos_recibidos = Signal(str)
    estado_conexion = Signal(bool, str)  # (Conectado?, Mensaje)

    def __init__(self, ip_address: str = "192.168.4.1", port: int = 5000):
        super().__init__()
        self.ip_address = ip_address
        self.port = port
        self.socket = None
        self._conectado = False
        self._hilo_escucha = None

    def connect(self, ip_address: str = None, port: int = None):
        """Establece la conexión con la ESP32 en un hilo no bloqueante."""
        if ip_address:
            self.ip_address = ip_address
        if port:
            self.port = port

        # Usamos un hilo para conectar sin congelar la UI si la ESP32 no responde
        threading.Thread(target=self._proceso_conexion, daemon=True).start()

    def _proceso_conexion(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5.0)  # Timeout de 5 segundos para intentar conectar
            sock.connect((self.ip_address, self.port))
            sock.settimeout(None)  # Quitar timeout para lectura continua

            self.socket = sock
            self._conectado = True

            # Notificar éxito a la UI
            self.estado_conexion.emit(True, f"Conectado a {self.ip_address}:{self.port}")

            # Iniciar escucha continua automáticamente
            self.receive_data()

        except Exception as error:
            self._conectado = False
            self.socket = None
            self.estado_conexion.emit(False, f"Error al conectar: {error}")

    def disconnect(self):
        """Cierra la conexión con la ESP32."""
        self._conectado = False
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
                self.socket.close()
            except Exception:
                pass
            self.socket = None

        self.estado_conexion.emit(False, "Desconectado")

    def send_data(self, comando: str):

        pass