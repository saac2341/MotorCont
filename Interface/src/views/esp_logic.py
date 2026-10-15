from __future__ import annotations

import sys

import serial
from serial import SerialException
from serial.tools import list_ports

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QPlainTextEdit,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from forms.ESP32_ui import Ui_Form


class ESP32Logic(QWidget):
    """Interfaz para comunicación serial con un ESP32."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.serial_connection: serial.Serial | None = None

        self._crear_controles()
        self._conectar_eventos()
        self._actualizar_puertos()

        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self._leer_datos)

    def _crear_controles(self):
        layout = QVBoxLayout(self.ui.widget)

        self.port_combo = QComboBox()
        self.port_combo.setStyleSheet("color: white;")

        self.baud_spin = QSpinBox()
        self.baud_spin.setRange(300, 921600)
        self.baud_spin.setValue(115200)
        self.baud_spin.setStyleSheet("color: white;")

        self.refresh_button = QPushButton("Actualizar puertos")
        self.connect_button = QPushButton("Conectar")
        self.clear_button = QPushButton("Limpiar")

        self.status_label = QLabel("Desconectado")
        self.status_label.setStyleSheet("color: white;")

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet(
            "color: white; background-color: rgb(15, 18, 42);"
        )

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Puerto:"))
        controls.addWidget(self.port_combo)
        controls.addWidget(QLabel("Baudios:"))
        controls.addWidget(self.baud_spin)
        controls.addWidget(self.refresh_button)
        controls.addWidget(self.connect_button)
        controls.addWidget(self.clear_button)

        layout.addLayout(controls)
        layout.addWidget(self.status_label)
        layout.addWidget(self.output)

    def _conectar_eventos(self):
        self.refresh_button.clicked.connect(self._actualizar_puertos)
        self.connect_button.clicked.connect(self._alternar_conexion)
        self.clear_button.clicked.connect(self.output.clear)

    def _actualizar_puertos(self):
        puerto_actual = self.port_combo.currentData()

        self.port_combo.clear()

        for puerto in list_ports.comports():
            descripcion = f"{puerto.device} - {puerto.description}"
            self.port_combo.addItem(descripcion, puerto.device)

        if puerto_actual:
            indice = self.port_combo.findData(puerto_actual)
            if indice >= 0:
                self.port_combo.setCurrentIndex(indice)

        if self.port_combo.count() == 0:
            self.status_label.setText("No se encontraron puertos seriales")

    def _alternar_conexion(self):
        if self.serial_connection and self.serial_connection.is_open:
            self._desconectar()
        else:
            self._conectar()

    def _conectar(self):
        puerto = self.port_combo.currentData()

        if not puerto:
            self.status_label.setText("Selecciona un puerto serial")
            return

        try:
            self.serial_connection = serial.Serial(
                port=puerto,
                baudrate=self.baud_spin.value(),
                timeout=0,
            )

            self.timer.start()
            self.connect_button.setText("Desconectar")
            self.status_label.setText(f"Conectado a {puerto}")

        except SerialException as error:
            self.serial_connection = None
            self.status_label.setText(f"Error: {error}")

    def _desconectar(self):
        self.timer.stop()

        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

        self.connect_button.setText("Conectar")
        self.status_label.setText("Desconectado")

    def _leer_datos(self):
        if not self.serial_connection or not self.serial_connection.is_open:
            return

        try:
            while self.serial_connection.in_waiting:
                data = self.serial_connection.readline()

                if data:
                    texto = data.decode("utf-8", errors="replace").rstrip()
                    self.output.appendPlainText(texto)

        except SerialException as error:
            self.status_label.setText(f"Error de lectura: {error}")
            self._desconectar()

    def closeEvent(self, event):
        self._desconectar()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ESP32Logic()
    window.show()
    sys.exit(app.exec())
    