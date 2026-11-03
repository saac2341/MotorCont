"""Vista y lógica de procesamiento de filtros."""

import csv
import json
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMessageBox

from forms.filtros import Ui_Form
from src.views.base_view import BaseView


class FiltrosLogic(BaseView):
    """Vista de filtros conectada al hub principal."""

    def __init__(self, contenedor, hub=None):
        super().__init__(contenedor, hub=hub)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._datos_recibidos: list[float] = []
        self._datos_filtrados: list[float] = []
        self._conectado = False

        self.ui.textEdit.setReadOnly(True)
        self.ui.spinBox.setMinimum(1)
        self.ui.spinBox.setValue(5)

        self.ui.radioButton.setChecked(True)

        self.ui.pushButton.clicked.connect(self._exportar_csv)
        self.ui.pushButton_2.clicked.connect(self._exportar_json)

    def recibir_datos(self, datos: str):
        """Recibe datos desde el hub y actualiza la muestra original."""
        try:
            muestra = float(datos.strip())
        except (TypeError, ValueError):
            return

        self._datos_recibidos.append(muestra)
        self.ui.textEdit.append(str(muestra))
        self._actualizar_filtro()

    def set_conectado(self, ok: bool):
        """Actualiza el estado visual de la vista."""
        self._conectado = ok
        estado = "Conectado" if ok else "Desconectado"
        self.ui.label.setText(f"Editor de filtros de la muestra - {estado}")

    def _actualizar_filtro(self):
        """Aplica el filtro seleccionado sobre las muestras recibidas."""
        ventana = self.ui.spinBox.value()
        datos = self._datos_recibidos

        if not datos:
            return

        bajas = self._filtro_pasa_bajas(datos, ventana)
        altas = [
            original - filtrada
            for original, filtrada in zip(datos, bajas)
        ]

        if self.ui.radioButton.isChecked():
            resultado = bajas
        elif self.ui.radioButton_2.isChecked():
            resultado = altas
        else:
            resultado = [
                baja + alta
                for baja, alta in zip(bajas, altas)
            ]

        self._datos_filtrados = resultado
        self._mostrar_datos(self.ui.widget_2, resultado)

    @staticmethod
    def _filtro_pasa_bajas(datos: list[float], ventana: int) -> list[float]:
        """Calcula un promedio móvil de ventana configurable."""
        resultado = []

        for indice in range(len(datos)):
            inicio = max(0, indice - ventana + 1)
            valores = datos[inicio:indice + 1]
            resultado.append(sum(valores) / len(valores))

        return resultado

    def _mostrar_datos(self, widget, datos: list[float]):
        """Actualiza la representación textual del resultado filtrado."""
        widget.setToolTip(
            "\n".join(f"{valor:.6f}" for valor in datos[-100:])
        )

    def _exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar CSV",
            "",
            "CSV (*.csv)",
        )

        if not ruta:
            return

        try:
            with Path(ruta).open("w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["original", "filtrado"])

                for original, filtrado in zip(
                    self._datos_recibidos,
                    self._datos_filtrados,
                ):
                    escritor.writerow([original, filtrado])
        except OSError as error:
            QMessageBox.critical(
                self,
                "Error de exportación",
                f"No fue posible crear el archivo:\n{error}",
            )

    def _exportar_json(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar JSON",
            "",
            "JSON (*.json)",
        )

        if not ruta:
            return

        contenido = {
            "datos_originales": self._datos_recibidos,
            "datos_filtrados": self._datos_filtrados,
            "ventana": self.ui.spinBox.value(),
        }

        try:
            with Path(ruta).open("w", encoding="utf-8") as archivo:
                json.dump(contenido, archivo, indent=2)
        except OSError as error:
            QMessageBox.critical(
                self,
                "Error de exportación",
                f"No fue posible crear el archivo:\n{error}",
            )