"""2 capa desarrollo del HUB de la fuente y distribuyendolo por la interfaz de usuario."""

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QHBoxLayout,
)

from forms.main_window_ui import Ui_MainWindow
from src.fuentes import FuenteTCP


class MainWindow(QMainWindow):
    """Clase HUB central de la interfaz de usuario, que maneja la lógica de la ventana principal y la interacción con la fuente de datos."""

    datos_recibidos = Signal(
        str
    )  # Señal para transmitir datos recibidos a otras interfaces
    estado_conexion = Signal(
        bool, str
    )  # Señal para transmitir el estado de la conexión a otras interfaces

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fuente = FuenteTCP()  # Instancia de la fuente de datos TCP
        self._modulos = []  # Lista para almacenar los módulos secundarios

        self._configurar_interfaz()
        self._conectar_evento()
        self._cargar_modulos()

    def _configurar_interfaz(self):
        """Configura la interfaz de usuario, incluyendo la disposición de widgets y la inicialización de elementos."""
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(
            ["800", "5000", "6000", "7000"]
        )  # Agrega opciones de puerto al comboBox
        self.ui.comboBox.setEditable(
            True
        )  # Permite que el usuario ingrese un puerto personalizado
        self.ui.comboBox.setCurrentText(
            "5000"
        )  # Establece el puerto predeterminado en el comboBox
        self.ui.lineEdit.setPlaceholderText(
            "Dirección IP"
        )  # Establece un texto predeterminado en el campo de dirección IP
        self.ui.lineEdit.setText(
            "192.168.1.1"
        )  # Establece un texto predeterminado en el campo de dirección IP
        self.ui.label_2.setText(
            "Estado: Desconectado"
        )  # Establece el estado inicial de la conexión
        self.ui.pushButton_5.setText(
            "Conectar"
        )  # Establece el texto del botón de conexión

    def _conectar_evento(self):
        """Configuración de los eventos en la ventana principal."""
        self.ui.btnFiltro.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentIndex(
                self.ui.pagWidget.indexOf(self.ui.page_Filtt)
            )
        )
        self.ui.btnImpulse.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentIndex(
                self.ui.pagWidget.indexOf(self.ui.page_Impulse)
            )
        )
        self.ui.btnESP32.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentIndex(
                self.ui.pagWidget.indexOf(self.ui.page_esp)
            )
        )
        self.ui.default_2.clicked.connect(
            lambda: self.ui.pagWidget.setCurrentIndex(
                self.ui.pagWidget.indexOf(self.ui.frame_default)
            )
        )
        self.ui.pushButton_5.clicked.connect(
            self._alternar_conexion_tcp
        )  # Conecta el botón de conexión a la función de alternancia de conexión

        self.ui.btnDesconec.clicked.connect(
            self._desconectar_fuente
        )  # Conecta el botón de desconexión a la función de desconexión de la fuente

    def set_fuente(self, fuente):
        """Establece la fuente de datos para la ventana principal."""
        if self._fuente is not None:
            try:
                self._fuente.desconectar()  # Desconecta la fuente anterior si existe
            except Exception:
                pass
            self._fuente.deleteLater()  # Elimina la fuente anterior de manera segura

        self._fuente = fuente  # Asigna la nueva fuente de datos
        fuente.datos_recibidos.connect(
            self._procesar_datos.emit
        )  # Conecta la señal de datos recibidos de la fuente a la función de procesamiento de datos
        fuente.estado_conexion.connect(
            self._estado_conexion.emit
        )  # Conecta la señal de estado de conexión de la fuente a la función de actualización de estado
        fuente.estado_conexion.connect(
            self._actualizar_estado_conexion
        )  # Conecta la señal de estado de conexión de la fuente a la función de actualización de estado
        fuente.conectar()  # Inicia la conexión de la fuente de datos

    def enviar(self, comando: str):
        """Aqui los modulos enviaran los comandos a las ESP32, Filtro y Impulse"""
        if self._fuente and self._fuente.activa:
            self._fuente.enviar(
                comando
            )  # Envía el comando a la fuente de datos si está activa

    def registrar_modulo(self, modulo):
        """Registra el modulo donde recibe datos y estados"""
        self._modulos.append(
            modulo
        )  # Agrega el módulo a la lista de módulos registrados
        if hasattr(modulo, "recibir_datos"):
            self.datos_recibidos.connect(
                modulo.recibir_datos
            )  # Conecta la señal de datos recibidos a la función del módulo si existe
        if hasattr(modulo, "set_conectado"):
            self.estado_conexion.connect(
                modulo.set_conectado
            )  # Conecta la señal de estado de conexión a la función del módulo si existe
        if hasattr(modulo, "comando_solicitado"):
            modulo.comando_solicitado.connect(
                self.enviar
            )  # Conecta la señal de comando solicitado del módulo a la función de envío de comandos

    def _alternar_conexion_tcp(self):
        """Alterna la conexión TCP entre conectada y desconectada."""
        if self._fuente and self._fuente.activa:
            self._fuente.desconectar()  # Desconecta la fuente si está activa
            self._fuente = None  # Establece la fuente a None después de desconectar
            return
        ip = (
            self.ui.lineEdit.text().strip()
        )  # Obtiene la dirección IP del campo de texto y elimina espacios en blanco

        try:
            puerto = int(self.ui.comboBox.currentText().strip())
            if not 1 <= puerto <= 65535:
                raise ValueError
        except ValueError:
            self.ui.label_2.setText("Puerto Invalido")
            return
        if not ip:
            self.ui.label_2.setText("Escribre una IP")
            return

        self.ui.label_2.setText(
            f"Conectando a {ip}:{puerto}..."
        )  # Actualiza el estado de la conexión en la interfaz de usuario
        self.ui.pushButton_5.setEnabled(
            False
        )  # Desactiva el botón de conexión mientras se intenta conectar
        self.set_fuente(
            FuenteTCP(ip=ip, puerto=puerto)
        )  # Establece la fuente de datos TCP con la dirección IP y el puerto especificados

    def _actualizar_estado_ui(self, ok, mensaje):
        self.ui.label_2.setText(
            mensaje
        )  # Actualiza el estado de la conexión en la interfaz de usuario
        self.ui.pushButton_5.setEnabled(
            True
        )  # Reactiva el botón de conexión después de intentar conectar
        self.ui.pushButton_5.setText(
            "Desconectar" if ok else "Conectar"
        )  # Cambia el texto del botón de conexión según el estado de la conexión

    def _desconectar_fuente(self):
        if self.fuente:
            self._fuente.desconectar()  # Desconecta la fuente de datos si existe
            self._fuente = None  # Establece la fuente a None después de desconectar

    def _cargar_modulos(self):
        self.filtro = self._crear_modulo(
            "src.views.filtters_logic",
            "FiltrosLogic",
            self.ui.page_Filtt,
        )

        self.impulse = self._crear_modulo(
            "src.views.impulse_logic",
            "ImpulseLogic",
            self.ui.page_Impulse,
        )

        self.esp32 = self._crear_modulo(
            "src.views.ESP32Logic",
            "ESP32Logic",
            self.ui.page_esp,
        )

        self.senales = self._crear_modulo(
            "src.views.default_logic",
            "DefaultView",
            self.ui.page_Senal,
        )

    def _crear_modulo(self, modulo, clase, contenedor):
        try:
            module = __import__(modulo, fromlist=[clase])
            widget_class = getattr(module, clase)
            widget = widget_class(contenedor, hub=self)

            layout = QVBoxLayout(contenedor)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(widget)

            self.registrar_modulo(
                widget
            )  # Registra el módulo para recibir datos y estados
            return widget
        except Exception as e:
            label = QLabel(f"Modulo {clase} no disponible: {e}", contenedor)
            label.setStyleSheet("color: white;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            QVBoxLayout(contenedor).addWidget(label)
            return None

    # Cierre de la clase MainWindow
    def closeEvent(self, event):
        self._desconectar_todo()
        self._desconectar_fuente()
        event.accept()  # Acepta el evento de cierre para cerrar la ventana
