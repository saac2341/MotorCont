# src/views/components/goniometro_widget.py
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QWidget


class GoniometroWidget(QWidget):
    """Widget vectorial para visualizar ángulos (0° a 180° o -90° a +90°)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._angulo = 0.0  # Ángulo actual en grados (-90 a 90)
        self.setMinimumSize(200, 150)

    def set_angulo(self, angulo: float):
        """Actualiza el ángulo del goniómetro (-90° a +90°)."""
        self._angulo = max(-90.0, min(90.0, float(angulo)))
        self.update()  # Redibuja el widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        ancho = self.width()
        alto = self.height()
        centro = QPointF(ancho / 2, alto * 0.85)
        radio = min(ancho / 2.2, alto * 0.75)

        # 1. Fondo / Arco principal
        rect_arco = QRectF(centro.x() - radio, centro.y() - radio, radio * 2, radio * 2)
        pen_arco = QPen(QColor("#2563eb"), 4)
        painter.setPen(pen_arco)
        # Dibujar semicírculo (desde 0° hasta 180° en unidades de 1/16 de grado)
        painter.drawArc(rect_arco, 0 * 16, 180 * 16)

        # 2. Marcas de graduación (-90° a +90°)
        painter.setPen(QPen(QColor("#ffffff"), 1))
        for deg in range(-90, 91, 15):
            rad = Qt.radians(deg - 90)  # Convertir a radianes con offset
            r_int = radio - (12 if deg % 30 == 0 else 6)
            p1 = QPointF(centro.x() + radio * Qt.cos(rad), centro.y() + radio * Qt.sin(rad))
            p2 = QPointF(centro.x() + r_int * Qt.cos(rad), centro.y() + r_int * Qt.sin(rad))
            painter.drawLine(p1, p2)

        # 3. Aguja
        rad_aguja = Qt.radians(self._angulo - 90)
        p_aguja = QPointF(
            centro.x() + (radio - 15) * Qt.cos(rad_aguja),
            centro.y() + (radio - 15) * Qt.sin(rad_aguja),
        )
        pen_aguja = QPen(QColor("#ff7800"), 3)
        painter.setPen(pen_aguja)
        painter.drawLine(centro, p_aguja)

        # Pivote central
        painter.setBrush(QColor("#ff7800"))
        painter.drawEllipse(centro, 6, 6)

        # 4. Texto digital
        painter.setPen(QColor("#ffffff"))
        painter.setFont(QFont("Bahnschrift", 12, QFont.Bold))
        painter.drawText(
            QRectF(0, alto * 0.88, ancho, 25),
            Qt.AlignCenter,
            f"{self._angulo:.1f}°",
        )