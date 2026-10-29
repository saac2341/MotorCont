from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QSettings, QUrl
from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
    QVBoxLayout,
    QLabel,
    QWidget,
)

from forms.edgeImpulse_ui import Ui_Form


class EdgeImpulseLogic(QWidget):
    """Lógica de la interfaz Edge Impulse."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.settings = QSettings("MotorCont", "Interface")
        self.archivos: list[Path] = []

        self._configurar_interfaz()
        self._conectar_eventos()
        self._cargar_datos_guardados()
        self._establecer_estado("neutral")

    def _configurar_interfaz(self):
        self.ui.line_Token.setEchoMode(
            self.ui.line_Token.EchoMode.Password
        )

        self.ui.table_archive.setColumnCount(2)
        self.ui.table_archive.setHorizontalHeaderLabels(
            ["Archivo", "Ruta"]
        )
        self.ui.table_archive.horizontalHeader().setStretchLastSection(True)
        self.ui.table_archive.setSelectionBehavior(
            self.ui.table_archive.SelectionBehavior.SelectRows
        )
        self.ui.table_archive.setEditTriggers(
            self.ui.table_archive.EditTrigger.NoEditTriggers
        )

        serial_layout = QVBoxLayout(self.ui.widget_Serial)
        serial_layout.setContentsMargins(12, 8, 12, 8)

        self.serial_status = QLabel("Puerto serial desconectado")
        self.serial_status.setStyleSheet("color: white;")
        serial_layout.addWidget(self.serial_status)

        self.ui.push_reboot.setEnabled(False)
        self.ui.push_anals.setEnabled(False)

    def _conectar_eventos(self):
        self.ui.push_connect.clicked.connect(self._conectar_edge_impulse)
        self.ui.push_cancel.clicked.connect(self._cancelar)
        self.ui.push_upinf.clicked.connect(self._seleccionar_archivo)
        self.ui.push_reboot.clicked.connect(self._actualizar)
        self.ui.push_anals.clicked.connect(self._analizar_archivo)
        self.ui.list_Archive.currentRowChanged.connect(
            self._seleccionar_archivo_lista
        )

    def _cargar_datos_guardados(self):
        token = self.settings.value("edge_impulse/token", "", type=str)

        if token:
            self.ui.line_Token.setText(token)

        archivos = self.settings.value("edge_impulse/archivos", [], type=list)

        for archivo in archivos:
            ruta = Path(archivo)
            if ruta.exists():
                self._agregar_archivo(ruta)

    def _conectar_edge_impulse(self):
        token = self.ui.line_Token.text().strip()

        if not token:
            self._mostrar_error("Debes ingresar un token de Edge Impulse.")
            self._establecer_estado("error")
            return

        self.settings.setValue("edge_impulse/token", token)

        self._establecer_estado("ok")
        self.ui.push_connect.setEnabled(False)
        self.ui.push_reboot.setEnabled(True)
        self.ui.push_anals.setEnabled(bool(self.archivos))
        self.serial_status.setText("Token configurado correctamente")

        # Página pública de Edge Impulse.
        self.ui.webpageImpulse.setUrl(
            QUrl("https://studio.edgeimpulse.com")
        )

    def _seleccionar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            str(Path.home()),
            "Archivos de datos (*.csv *.json *.txt *.zip);;"
            "Todos los archivos (*)",
        )

        if ruta:
            self._agregar_archivo(Path(ruta))

    def _agregar_archivo(self, ruta: Path):
        if ruta in self.archivos:
            return

        self.archivos.append(ruta)

        self.ui.list_Archive.addItem(ruta.name)

        fila = self.ui.table_archive.rowCount()
        self.ui.table_archive.insertRow(fila)
        self.ui.table_archive.setItem(
            fila, 0, QTableWidgetItem(ruta.name)
        )
        self.ui.table_archive.setItem(
            fila, 1, QTableWidgetItem(str(ruta))
        )

        self.ui.push_anals.setEnabled(True)
        self._guardar_archivos()

    def _seleccionar_archivo_lista(self, fila: int):
        if 0 <= fila < len(self.archivos):
            self.ui.table_archive.selectRow(fila)

    def _actualizar(self):
        self.ui.list_Archive.clear()
        self.ui.table_archive.setRowCount(0)

        archivos_validos = [
            ruta for ruta in self.archivos if ruta.exists()
        ]

        self.archivos.clear()

        for ruta in archivos_validos:
            self._agregar_archivo(ruta)

        self.ui.webpageImpulse.reload()
        self.serial_status.setText("Lista y página actualizadas")

    def _analizar_archivo(self):
        fila = self.ui.table_archive.currentRow()

        if fila < 0 or fila >= len(self.archivos):
            self._mostrar_error("Selecciona un archivo para analizar.")
            return

        archivo = self.archivos[fila]

        self._establecer_estado("process")
        self.serial_status.setText(
            f"Archivo seleccionado para análisis: {archivo.name}"
        )

        QMessageBox.information(
            self,
            "Análisis",
            f"El archivo está listo para ser analizado:\n\n{archivo}",
        )

        self._establecer_estado("ok")

    def _cancelar(self):
        self.ui.line_Token.clear()
        self.ui.list_Archive.clear()
        self.ui.table_archive.setRowCount(0)
        self.ui.webpageImpulse.setUrl(QUrl("about:blank"))

        self.archivos.clear()
        self.settings.remove("edge_impulse/token")
        self.settings.remove("edge_impulse/archivos")

        self.ui.push_connect.setEnabled(True)
        self.ui.push_reboot.setEnabled(False)
        self.ui.push_anals.setEnabled(False)

        self.serial_status.setText("Configuración cancelada")
        self._establecer_estado("neutral")

    def _guardar_archivos(self):
        self.settings.setValue(
            "edge_impulse/archivos",
            [str(ruta) for ruta in self.archivos],
        )

    def _establecer_estado(self, estado: str):
        leds = {
            "ok": self.ui.kled_ok,
            "neutral": self.ui.kled_neutral,
            "process": self.ui.kled_process,
        }

        for nombre, led in leds.items():
            try:
                led.setState(nombre == estado)
            except AttributeError:
                led.setEnabled(nombre == estado)

    def _mostrar_error(self, mensaje: str):
        QMessageBox.warning(self, "Edge Impulse", mensaje)
        self.serial_status.setText(mensaje)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ventana = EdgeImpulseLogic()
    ventana.resize(1046, 632)
    ventana.show()
    sys.exit(app.exec())