from __future__ import annotations

import sys

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtNetwork import QAbstractSocket, QTcpSocket
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from forms.main_window_ui import Ui_MainWindow


class MainWindowLogic(QMainWindow):
    """Controlador principal de la aplicación."""

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.socket = QTcpSocket(self)
        self._configurar_interfaz()
        self._cargar_interfaces()
        self._conectar_eventos()

    def _configurar_interfaz(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(["80", "8080", "5000", "3333"])
        self.ui.comboBox.setEditable(True)
        self.ui.comboBox.setCurrentText("5000")

        self.ui.lineEdit.setPlaceholderText("Dirección IP del dispositivo")
        self.ui.lineEdit.setText("192.168.4.1")

        self.ui.label_2.setText("Conectar dirección IP")

    def _cargar_interfaces(self):
        """Carga las interfaces secundarias dentro del QStackedWidget."""
        self.filtro = self._crear_interfaz(
            "src.views.filtros_logic",
            "FiltrosLogic",
            self.ui.page_Filtt,
            "Interfaz de filtros no disponible",
        )

        self.impulse = self._crear_interfaz(
            "src.views.edgeImpulse_logic",
            "EdgeImpulseLogic",
            self.ui.page_Impulse,
            "Interfaz Edge Impulse no disponible",
        )

        self.esp32 = self._crear_interfaz(
            "src.views.ESP32_logic",
            "ESP32Logic",
            self.ui.page_esp,
            "Interfaz ESP32 no disponible",
        )

        self._mostrar_mensaje(
            self.ui.pageSenal,
            "Interfaz de señal pendiente de implementar",
        )

    def _crear_interfaz(
        self,
        modulo: str,
        clase: str,
        contenedor: QWidget,
        mensaje: str,
    ):
        try:
            module = __import__(modulo, fromlist=[clase])
            widget_class = getattr(module, clase)
            widget = widget_class(contenedor)

            layout = QVBoxLayout(contenedor)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(widget)

            return widget

        except (ImportError, AttributeError, TypeError) as error:
            self._mostrar_mensaje(contenedor, f"{mensaje}\n\n{error}")
            return None

    def _mostrar_mensaje(self, contenedor: QWidget, texto: str):
        layout = QVBoxLayout(contenedor)
        label = QLabel(texto)
        label.setStyleSheet("color: white;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

    def _conectar_eventos(self):
        self.ui.btnFiltro.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentWidget(self.ui.page_Filtt)
        )

        self.ui.btnImpulse.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentWidget(self.ui.page_Impulse)
        )

        self.ui.btnESP32.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentWidget(self.ui.page_esp)
        )

        self.ui.pushButton_5.clicked.connect(self._alternar_conexion)
        self.ui.btnDesconec.clicked.connect(self.close)

        self.socket.connected.connect(self._conexion_exitosa)
        self.socket.disconnected.connect(self._conexion_cerrada)
        self.socket.errorOccurred.connect(self._error_conexion)

    def _alternar_conexion(self):
        if self.socket.state() == QAbstractSocket.SocketState.ConnectedState:
            self.socket.disconnectFromHost()
            return

        ip = self.ui.lineEdit.text().strip()
        puerto_texto = self.ui.comboBox.currentText().strip()

        if not ip:
            self.ui.label_2.setText("Escribe una dirección IP")
            return

        try:
            puerto = int(puerto_texto)
            if not 1 <= puerto <= 65535:
                raise ValueError
        except ValueError:
            self.ui.label_2.setText("El puerto no es válido")
            return

        self.ui.label_2.setText(f"Conectando con {ip}:{puerto}...")
        self.ui.pushButton_5.setEnabled(False)

        self.socket.connectToHost(ip, puerto)

        QTimer.singleShot(
            5000,
            lambda: self._cancelar_conexion_si_pendiente(),
        )

    def _cancelar_conexion_si_pendiente(self):
        if self.socket.state() == QAbstractSocket.SocketState.ConnectingState:
            self.socket.abort()
            self.ui.pushButton_5.setEnabled(True)
            self.ui.label_2.setText("Tiempo de conexión agotado")

    def _conexion_exitosa(self):
        ip = self.ui.lineEdit.text()
        puerto = self.ui.comboBox.currentText()

        self.ui.label_2.setText(f"Conectado: {ip}:{puerto}")
        self.ui.pushButton_5.setText("Desconectar")
        self.ui.pushButton_5.setEnabled(True)

    def _conexion_cerrada(self):
        self.ui.label_2.setText("Desconectado")
        self.ui.pushButton_5.setText("Conectar")
        self.ui.pushButton_5.setEnabled(True)

    def _error_conexion(self, error):
        self.ui.label_2.setText(
            f"Error de conexión: {self.socket.errorString()}"
        )
        self.ui.pushButton_5.setText("Conectar")
        self.ui.pushButton_5.setEnabled(True)

    def closeEvent(self, event):
        if self.socket.state() != QAbstractSocket.SocketState.UnconnectedState:
            self.socket.disconnectFromHost()

        event.accept()


if __name__ == "__main__":
    from PySide6.QtCore import Qt

    app = QApplication(sys.argv)
    window = MainWindowLogic()
    window.show()
    sys.exit(app.exec())
    