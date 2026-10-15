import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Importamos directamente la clase visual compilada
from forms.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Construye todos los widgets creados en Qt Designer
        self.setupUi(self)

        # 2. Establecer la página inicial (Página 0: Señal)
        self.pagWidget.setCurrentIndex(0)

        # 3. Conectar la navegación lateral y acciones
        self.setup_signals()

    def setup_signals(self):
        """Asigna eventos (slots) a los widgets definidos en el archivo UI."""
        # Cambio de páginas en QStackedWidget
        self.btnFiltro.clicked.connect(lambda: self.pagWidget.setCurrentIndex(1))
        self.btnImpulse.clicked.connect(lambda: self.pagWidget.setCurrentIndex(2))
        self.btnESP32.clicked.connect(lambda: self.pagWidget.setCurrentIndex(3))
        
        # Botón Exit
        self.btnDesconec.clicked.connect(self.close)

        # Botón Conectar (panel superior)
        self.pushButton_5.clicked.connect(self.on_conectar_clicked)

    def on_conectar_clicked(self):
        """Extrae la configuración de red al presionar 'Conectar'."""
        ip = self.lineEdit.text().strip()
        frecuencia = self.comboBox.currentText()
        print(f"[UI] Intentando conectar con ESP32 en {ip} a {frecuencia}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.setWindowTitle("ESP32 + Edge Impulse Dashboard")
    window.show()
    
    sys.exit(app.exec())