# Widgrt encargado de visualizar una gráfica de tiempo real optimizada con PyQtGraph.
from collections import deque
import time

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QVBoxLayout, QWidget
import pyqtgraph as pg


class GraficaTiempoWidget(QWidget):
    """Widget de gráfica de líneas vs. tiempo real optimizado con PyQtGraph."""

    def __init__(self, parent=None, ventana_tiempo_seg: float = 10.0, titulo: str = ""):
        super().__init__(parent)

        self.ventana_tiempo = ventana_tiempo_seg
        self.tiempo_inicio = time.time()

        # Buffers de datos usando deque para rendimiento O(1)
        self.tiempos = deque()
        self.valores = deque()

        self._configurar_interfaz(titulo)

    def _configurar_interfaz(self, titulo: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Configuración estética de PyQtGraph (acorde al tema oscuro de la UI)
        pg.setConfigOption("background", "#191d3f")
        pg.setConfigOption("foreground", "#e5e7eb")

        self.plot_widget = pg.PlotWidget(title=f"<b>{titulo}</b>")
        self.plot_widget.showGrid(x=True, y=True, alpha=0.2)
        self.plot_widget.setLabel("bottom", "Tiempo", units="s")
        self.plot_widget.setLabel("left", "Amplitud")

        # Curva con antialiasing y estilo de trazo
        self.curva = self.plot_widget.plot(
            pen=pg.mkPen(color="#ff7800", width=2),
            name="Señal",
        )

        layout.addWidget(self.plot_widget)

    def agregar_punto(self, valor: float, timestamp: float | None = None):
        """Agrega una nueva muestra recibida y actualiza la ventana temporal."""
        t_actual = (timestamp if timestamp is not None else time.time()) - self.tiempo_inicio

        self.tiempos.append(t_actual)
        self.valores.append(valor)

        # Descartar muestras fuera de la ventana de tiempo especificada
        while self.tiempos and (t_actual - self.tiempos[0] > self.ventana_tiempo):
            self.tiempos.popleft()
            self.valores.popleft()

        # Actualizar los vectores de renderizado
        self.curva.setData(list(self.tiempos), list(self.valores))

    def limpiar(self):
        """Limpia los buffers de la gráfica y reinicia la referencia de tiempo."""
        self.tiempos.clear()
        self.valores.clear()
        self.tiempo_inicio = time.time()
        self.curva.clear()