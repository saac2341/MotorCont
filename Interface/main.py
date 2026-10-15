import sys

from PySide6.QtWidgets import QApplication

from src.main_window import MainWindowLogic


def main():
    app = QApplication(sys.argv)

    ventana = MainWindowLogic()
    ventana.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())