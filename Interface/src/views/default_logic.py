"""Mudulo de señales - recibe datos del hub y los muestra en la ventana principal, ademas de enviar comandos a la fuente de datos."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout


from src.views.base_view import BaseView

class DefaultView(BaseView):
    def __init__(self, contenedor, hub = None):
        super().__init__(contenedor, hub = hub)
        from forms.default_ui import Ui_Form  # Importa la clase de la interfaz de usuario generada por Qt Designer
        self.ui = Ui_Form()  # Crea una instancia de la clase de la interfaz de usuario
        self.ui.setupUi(self)  # Configura la interfaz de usuario
        
        self.texto = self.ui.textEdit  # Área de texto para mostrar los datos recibidos
        self.texto.setReadOnly(True)  # Hace que el área de texto sea de solo lectura

        self._contador = 0  # Contador de datos recibidos
        self.texto = QTextEdit(readOnly = True)  # Área de texto para mostrar los datos recibidos
        self.texto.append("Esperando datos...")  # Mensaje inicial en el área de texto
        self.btn_ping = QPushButton("Enviar PING a la ESP32")  # Botón para enviar un comando PING a la fuente de datos
        self.btn_ping.setEnabled(False)  # Inicialmente deshabilitado hasta que se establezca la conexión

        self.btn_ping.clicked.connect(
            lambda: self.comando_solicitado.emit("PING")  # Conecta el botón de PING a la señal de comando solicitado
        )

        layout = QVBoxLayout(self)  # Layout principal vertical
        layout.addWidget(QLabel("Datos recibidos:"))  # Agrega un label al layout
        layout.addWidget(self.btn_ping)  # Agrega el botón de PING al layout
        layout.addWidget(self.texto)  # Agrega el área de texto al layout
        layout.addWidget(self.btn_ping)  # Agrega el botón de PING al layout nuevamente (posiblemente un error duplicado)

    def recibir_datos(self, datos: str):
        """Recibe datos de la fuente y los muestra en el área de texto."""
        self._contador += 1  # Incrementa el contador de datos recibidos
        self.texto.append(f"[{self._contador}] {datos}")  # Muestra los datos recibidos en el área de texto

    def set_conectado(self, ok: bool):
        self.texto.append(f"[fuente {'ON' if ok else 'OFF'}]")
        self.btn_ping.setEnabled(ok)