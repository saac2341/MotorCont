"""Punto de entrada de la aplicación MotorCont."""

import sys

from PySide6.QtWidgets import QApplication

from src.main_window_logic import MainWindow


def main() -> int:
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()

    return app.exec()

if __name__ == "__main__":
    main()
