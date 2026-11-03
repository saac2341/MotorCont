"""Vista de monitoreo de datos recibidos desde la ESP32."""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
)

from forms.ESP32_ui import Ui_Form
from src.views.base_view import BaseView


class ESP32Logic(BaseView):
    """Vista de datos seriales de la ESP32 conectada al hub."""

    def __init__(self, contenedor, hub=None):
        super().__init__(contenedor, hub=hub)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._contador = 0
        self._conectado = False

        self._crear_controles()
        self._configurar_eventos()

    def _crear_controles(self):
        """Crea los controles dentro del contenedor definido por Qt Designer."""
        self.salida = QPlainTextEdit(self.ui.widget)
        self.salida.setReadOnly(True)
        self.salida.setPlaceholderText(
            "Esperando datos de la ESP32..."
        )

        self.btn_ping = QPushButton("Enviar PING", self.ui.widget)
        self.btn_limpiar = QPushButton("Limpiar", self.ui.widget)
        self.btn_ping.setEnabled(False)

        controles = QHBoxLayout()
        controles.addWidget(self.btn_ping)
        controles.addWidget(self.btn_limpiar)

        layout = QVBoxLayout(self.ui.widget)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.addLayout(controles)
        layout.addWidget(self.salida)

    def _configurar_eventos(self):
        """Conecta las acciones de la vista con el hub."""
        self.btn_ping.clicked.connect(
            lambda: self.comando_solicitado.emit("PING")
        )
        self.btn_limpiar.clicked.connect(self.salida.clear)

    def recibir_datos(self, datos: str):
        """Muestra los datos recibidos desde el hub."""
        self._contador += 1
        self.salida.appendPlainText(
            f"[{self._contador}] {datos}"
        )

    def set_conectado(self, ok: bool):
        """Actualiza el estado de conexión de la ESP32."""
        self._conectado = ok
        self.btn_ping.setEnabled(ok)

        estado = "Conectada" if ok else "Desconectada"
        self.ui.label.setText(
            f"Serial Data de ESP32 - {estado}"
        )

