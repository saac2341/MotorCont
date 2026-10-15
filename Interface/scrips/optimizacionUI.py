import sys 
import subprocess

def optimize_ui():
    python_exe = sys.executable
    print ("Copilacion de interfaces y recursos de PySide6...")

    subprocess.run([python_exe, "-m", "pyside6-uic", "forms/ui/main_window.ui", "-o", "forms/main_window_ui.py"])
    subprocess.run([python_exe, "-m", "pyside6-uic", "forms/ui/filtros.ui", "-o", "forms/filtros_ui.py"])
    subprocess.run([python_exe, "-m", "pyside6-uic", "forms/ui/edgeImpulse.ui", "-o", "forms/edgeImpulse_ui.py"])
    subprocess.run([python_exe, "-m", "pyside6-uic", "forms/ui/ESP32.ui", "-o", "forms/ESP32_ui.py"])
    subprocess.run([python_exe, "-m", "pyside6-uic", "forms/ui/default.ui", "-o", "forms/default_ui.py"])

    subprocess.run([python_exe, "-m", "pyside6-rcc", "forms/recurces.qrc", "-o", "forms/recurces_rc.py"])

    print ("Compilacion de interfaces y recursos de PySide6 finalizada.")

    if __name__ == "__main__":
        optimize_ui()