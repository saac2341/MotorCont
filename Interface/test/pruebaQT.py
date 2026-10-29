import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def mostrar_mensaje():
    nombre = entrada.text().strip() or "usuario"
    etiqueta.setText(f"¡Hola, {nombre}!")


app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Interfaz de prueba")
ventana.resize(350, 180)

layout = QVBoxLayout()

titulo = QLabel("Prueba sencilla con PyQt6")
entrada = QLineEdit()
entrada.setPlaceholderText("Escribe tu nombre")

boton = QPushButton("Saludar")
boton.clicked.connect(mostrar_mensaje)

etiqueta = QLabel("Introduce tu nombre y pulsa el botón")

layout.addWidget(titulo)
layout.addWidget(entrada)
layout.addWidget(boton)
layout.addWidget(etiqueta)

ventana.setLayout(layout)
ventana.show()

sys.exit(app.exec())