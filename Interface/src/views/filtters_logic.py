from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np
import pyqtgraph as pg
from scipy.signal import butter, filtfilt

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from forms.filtros import Ui_Form


class FiltrosLogic(QWidget):
    """Editor y visualizador de filtros digitales."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data_original = np.array([], dtype=float)
        self.data_filtrada = np.array([], dtype=float)

        self._configurar_interfaz()
        self._conectar_eventos()

    def _configurar_interfaz(self):
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox.setValue(10)
        self.ui.spinBox.setToolTip("Frecuencia de corte")

        self.ui.textEdit.setPlaceholderText(
            "Introduce una muestra por línea o separada por comas..."
        )

        self.grafica_antes = pg.PlotWidget()
        self.grafica_despues = pg.PlotWidget()

        for grafica, titulo in (
            (self.grafica_antes, "Señal original"),
            (self.grafica_despues, "Señal filtrada"),
        ):
            grafica.setBackground("#191d3f")
            grafica.setTitle(titulo, color="white")
            grafica.showGrid(x=True, y=True, alpha=0.25)
            grafica.getAxis("left").setTextPen("white")
            grafica.getAxis("bottom").setTextPen("white")

        QVBoxLayout(self.ui.widget).addWidget(self.grafica_antes)
        QVBoxLayout(self.ui.widget_2).addWidget(self.grafica_despues)

        self.ui.radioButton.setChecked(True)

    def _conectar_eventos(self):
        self.ui.pushButton.clicked.connect(self.exportar_csv)
        self.ui.pushButton_2.clicked.connect(self.exportar_json)

        self.ui.radioButton.toggled.connect(self.aplicar_filtro)
        self.ui.radioButton_2.toggled.connect(self.aplicar_filtro)
        self.ui.radioButton_3.toggled.connect(self.aplicar_filtro)

        self.ui.spinBox.valueChanged.connect(self.aplicar_filtro)
        self.ui.textEdit.textChanged.connect(self.cargar_datos)

    def cargar_datos(self):
        """Lee muestras numéricas desde el editor de texto."""
        texto = self.ui.textEdit.toPlainText().strip()

        if not texto:
            self.data_original = np.array([], dtype=float)
            self.data_filtrada = np.array([], dtype=float)
            self._actualizar_graficas()
            return

        texto = texto.replace(",", " ").replace(";", " ")
        valores = []

        for valor in texto.split():
            try:
                valores.append(float(valor))
            except ValueError:
                continue

        self.data_original = np.asarray(valores, dtype=float)
        self.aplicar_filtro()

    def set_data(self, data):
        """Permite cargar datos desde otra interfaz o desde un sensor."""
        self.data_original = np.asarray(data, dtype=float)

        self.ui.textEdit.blockSignals(True)
        self.ui.textEdit.setPlainText(
            "\n".join(str(valor) for valor in self.data_original)
        )
        self.ui.textEdit.blockSignals(False)

        self.aplicar_filtro()

    def aplicar_filtro(self):
        """Aplica el filtro seleccionado a la señal."""
        if self.data_original.size < 5:
            self._actualizar_graficas()
            return

        try:
            orden = 3
            frecuencia_corte = self.ui.spinBox.value()
            frecuencia_muestreo = 1000.0

            frecuencia_normalizada = (
                frecuencia_corte / (frecuencia_muestreo / 2)
            )

            frecuencia_normalizada = max(
                0.001,
                min(0.999, frecuencia_normalizada),
            )

            if self.ui.radioButton.isChecked():
                tipo = "lowpass"
            elif self.ui.radioButton_2.isChecked():
                tipo = "highpass"
            else:
                tipo = "bandpass"

            if tipo == "bandpass":
                limites = [frecuencia_normalizada / 2,
                           frecuencia_normalizada]
                limites[0] = max(0.001, limites[0])
                limites[1] = min(0.999, limites[1])
                coef_b, coef_a = butter(
                    orden,
                    limites,
                    btype=tipo,
                )
            else:
                coef_b, coef_a = butter(
                    orden,
                    frecuencia_normalizada,
                    btype=tipo,
                )

            self.data_filtrada = filtfilt(
                coef_b,
                coef_a,
                self.data_original,
            )

        except ValueError:
            self.data_filtrada = self.data_original.copy()

        self._actualizar_graficas()

    def _actualizar_graficas(self):
        self.grafica_antes.clear()
        self.grafica_despues.clear()

        if self.data_original.size == 0:
            return

        eje_x = np.arange(self.data_original.size)

        self.grafica_antes.plot(
            eje_x,
            self.data_original,
            pen=pg.mkPen("#38bdf8", width=2),
        )

        if self.data_filtrada.size:
            self.grafica_despues.plot(
                eje_x,
                self.data_filtrada,
                pen=pg.mkPen("#f59e0b", width=2),
            )

    def exportar_csv(self):
        if not self.data_filtrada.size:
            self._mostrar_error("No hay datos filtrados para exportar.")
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar CSV",
            str(Path.home() / "muestra_filtrada.csv"),
            "Archivos CSV (*.csv)",
        )

        if not ruta:
            return

        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["muestra_original", "muestra_filtrada"])

            for original, filtrada in zip(
                self.data_original,
                self.data_filtrada,
            ):
                escritor.writerow([original, filtrada])

    def exportar_json(self):
        if not self.data_filtrada.size:
            self._mostrar_error("No hay datos filtrados para exportar.")
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar JSON",
            str(Path.home() / "muestra_filtrada.json"),
            "Archivos JSON (*.json)",
        )

        if not ruta:
            return

        datos = {
            "original": self.data_original.tolist(),
            "filtrada": self.data_filtrada.tolist(),
            "tipo": self._tipo_filtro(),
            "frecuencia_corte": self.ui.spinBox.value(),
        }

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)

    def _tipo_filtro(self):
        if self.ui.radioButton.isChecked():
            return "pasa_bajas"
        if self.ui.radioButton_2.isChecked():
            return "pasa_altas"
        return "combinado"

    def _mostrar_error(self, mensaje):
        QMessageBox.warning(self, "Filtros", mensaje)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiltrosLogic()
    ventana.show()
    sys.exit(app.exec())