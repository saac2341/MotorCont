### Modulo encargado del control del flujo de la aplicación y la carga de interfaces secundarias.

"""Contrato que los forms UI deben de 
cumplir para poder ser cargados en la ventana principal."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

class BaseView(QWidget):
    comando_solicitado = Signal(str)  # Señal para transmitir comandos solicitados a otras interfaces

    def __init__(self, contenedor, hub = None):
        super().__init__(contenedor)
        self.hub = hub  # Referencia al hub central de la aplicación

    def recibir_datos(self, datos: str):
        """Método que debe ser implementado por las vistas secundarias para recibir datos de la fuente."""
        raise NotImplementedError

    def set_conectado(self, ok: bool):
        """Método que debe ser implementado por las vistas secundarias para actualizar el estado de conexión."""
        raise NotImplementedError
    