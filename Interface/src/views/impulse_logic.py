"""Vista de integración con Edge Impulse."""

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QPlainTextEdit,
    QVBoxLayout,
)

from forms.edgeImpulse_ui import Ui_Form
from src.views.base_view import BaseView


class ImpulseLogic(BaseView):
    """Vista de Edge Impulse conectada al hub principal."""

    def __init__(self, contenedor, hub=None):
        super().__init__(contenedor, hub=hub)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._conectado = False
        self._archivo_seleccionado = None

        self._crear_terminal()
        self._configurar_eventos()

        self.ui.push_upinf.setEnabled(False)
        self.ui.push_reboot.setEnabled(False)
        self.ui.push_anals.setEnabled(False)
        self.ui.push_connect.setEnabled(False)
        self.ui.push_cancel.setEnabled(False)

        self.ui.webpageImpulse.setUrl(
            QUrl("https://studio.edgeimpulse.com")
        )

    def _crear_terminal(self):
        """Crea el visor de mensajes dentro del formulario diseñado."""
        self.terminal = QPlainTextEdit(self.ui.widget_Serial)
        self.terminal.setReadOnly(True)
        self.terminal.setPlaceholderText(
            "Esperando datos de Edge Impulse..."
        )

        layout = QVBoxLayout(self.ui.widget_Serial)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.addWidget(self.terminal)

    def _configurar_eventos(self):
        self.ui.push_upinf.clicked.connect(self._seleccionar_archivo)
        self.ui.push_reboot.clicked.connect(
            lambda: self._enviar_comando("IMPULSE_REFRESH")
        )
        self.ui.push_anals.clicked.connect(
            lambda: self._enviar_comando("IMPULSE_ANALYZE")
        )
        self.ui.push_connect.clicked.connect(
            lambda: self._enviar_comando("IMPULSE_CONNECT")
        )
        self.ui.push_cancel.clicked.connect(
            lambda: self._enviar_comando("IMPULSE_CANCEL")
        )

    def recibir_datos(self, datos: str):
        """Muestra los datos recibidos desde el hub."""
        self.terminal.appendPlainText(str(datos))

    def set_conectado(self, ok: bool):
        """Actualiza el estado de conexión de la vista."""
        self._conectado = ok

        botones = (
            self.ui.push_upinf,
            self.ui.push_reboot,
            self.ui.push_anals,
            self.ui.push_connect,
            self.ui.push_cancel,
        )

        for boton in botones:
            boton.setEnabled(ok)

        self.ui.kled_ok.setVisible(ok)
        self.ui.kled_neutral.setVisible(not ok)
        self.ui.kled_process.setVisible(False)

        self.ui.label.setText(
            f"Edge Impulse - {'Conectado' if ok else 'Desconectado'}"
        )

    def _seleccionar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo para Edge Impulse",
            "",
            "Archivos de datos (*.csv *.json *.txt);;Todos (*.*)",
        )

        if not ruta:
            return

        self._archivo_seleccionado = ruta
        self.terminal.appendPlainText(
            f"Archivo seleccionado: {ruta}"
        )
        self._enviar_comando(f"IMPULSE_UPLOAD:{ruta}")

    def _enviar_comando(self, comando: str):
        if not self._conectado:
            QMessageBox.warning(
                self,
                "Sin conexión",
                "La fuente de datos no está conectada.",
            )
            return

        self.ui.kled_process.setVisible(True)
        self.comando_solicitado.emit(comando)