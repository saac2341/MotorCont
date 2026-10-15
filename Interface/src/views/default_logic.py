from __future__ import annotations

import math
import random
from collections import deque

from PySide6.QtCore import QPainter, QPen, QTimer, Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QHBoxLayout, QWidget

from forms.default_ui import Ui_Form


class GraphWidget(QWidget):
    """Gráfica simple para mostrar los datos capturados."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.values = deque(maxlen=300)
        self.setMinimumHeight(100)

    def set_values(self, values):
        self.values = deque(values, maxlen=300)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.fillRect(self.rect(), QColor("#f6f5f4"))

        margin = 20
        area = self.rect().adjusted(margin, margin, -margin, -margin)

        painter.setPen(QPen(QColor("#cccccc"), 1))
        painter.drawRect(area)

        if len(self.values) < 2:
            return

        minimum = min(self.values)
        maximum = max(self.values)

        if minimum == maximum:
            minimum -= 1
            maximum += 1

        points = []
        width = area.width()
        height = area.height()

        for index, value in enumerate(self.values):
            x = area.left() + index * width / (len(self.values) - 1)
            y = area.bottom() - ((value - minimum) / (maximum - minimum)) * height
            points.append((int(x), int(y)))

        painter.setPen(QPen(QColor("#392f91"), 2))

        for first, second in zip(points, points[1:]):
            painter.drawLine(first[0], first[1], second[0], second[1])


class DefaultLogic(QWidget):
    """Lógica principal de la interfaz default."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.graph = GraphWidget(self.ui.widget_graf)
        graph_layout = QHBoxLayout(self.ui.widget_graf)
        graph_layout.setContentsMargins(0, 0, 0, 0)
        graph_layout.addWidget(self.graph)

        self.goniometer = GraphWidget(self.ui.widget_Gono)
        goniometer_layout = QHBoxLayout(self.ui.widget_Gono)
        goniometer_layout.setContentsMargins(0, 0, 0, 0)
        goniometer_layout.addWidget(self.goniometer)

        self.brain_activity = GraphWidget(self.ui.widget_3)
        brain_layout = QHBoxLayout(self.ui.widget_3)
        brain_layout.setContentsMargins(0, 0, 0, 0)
        brain_layout.addWidget(self.brain_activity)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self._capture_sample)

        self.samples = deque(maxlen=300)
        self.angle_samples = deque(maxlen=300)
        self.activity_samples = deque(maxlen=300)

        self.sample_number = 0
        self.is_capturing = False

        self.ui.pushButton_3.clicked.connect(self.start_capture)
        self.ui.pushButton_2.clicked.connect(self.stop_capture)
        self.ui.checkBox.toggled.connect(self._refresh_graph)

        self.stop_capture()

    def start_capture(self):
        """Inicia la captura de datos."""
        self.is_capturing = True
        self.timer.start()

        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.label_act.setText("Capturando datos...")

    def stop_capture(self):
        """Detiene la captura de datos."""
        self.is_capturing = False
        self.timer.stop()

        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.label_act.setText("Captura detenida")

    def _capture_sample(self):
        """Genera una muestra de prueba.

        Sustituye esta sección por la lectura del sensor real.
        """
        self.sample_number += 1

        angle = 45 + 35 * math.sin(self.sample_number / 12)
        angle += random.uniform(-2, 2)

        activity = 50 + 35 * math.sin(self.sample_number / 8)
        activity += random.uniform(-5, 5)
        activity = max(0, min(100, activity))

        self.update_data(angle, activity)

    def update_data(self, angle: float, activity: float):
        """Actualiza la interfaz con datos reales de los sensores."""
        angle = float(angle)
        activity = float(activity)

        self.samples.append(angle)
        self.angle_samples.append(angle)
        self.activity_samples.append(activity)

        self.ui.lcdIndicador.display(round(angle, 1))
        self.ui.label_act.setText(
            f"Actividad cerebral: {activity:.1f}%"
        )

        self._refresh_graph()

    def _refresh_graph(self):
        values = list(self.samples)

        if self.ui.checkBox.isChecked() and values:
            minimum = min(values)
            maximum = max(values)
            if minimum != maximum:
                values = [
                    (value - minimum) / (maximum - minimum) * 100
                    for value in values
                ]

        self.graph.set_values(values)
        self.goniometer.set_values(self.angle_samples)
        self.brain_activity.set_values(self.activity_samples)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = DefaultLogic()
    window.show()
    sys.exit(app.exec())