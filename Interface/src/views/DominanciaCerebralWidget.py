# src/views/components/dominancia_widget.py
from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QColor, QFont, QLinearGradient, QPainter, QPen
from PySide6.QtWidgets import QWidget


class DominanciaCerebralWidget(QWidget):
    """Widget con indicadores luminosos de actividad/dominancia hemisférica."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._nivel_izq = 0.0  # 0.0 a 1.0
        self._nivel_der = 0.0  # 0.0 a 1.0
        self.setMinimumSize(220, 100)

    def set_niveles(self, nivel_izq: float, nivel_der: float):
        """Actualiza los niveles de actividad (valores normalizados entre 0.0 y 1.0)."""
        self._nivel_izq = max(0.0, min(1.0, float(nivel_izq)))
        self._nivel_der = max(0.0, min(1.0, float(nivel_der)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        ancho = self.width()
        alto = self.height()
        radio_led = min(ancho / 6, alto / 3)

        # Posiciones de los indicadores LED
        centro_izq = (ancho * 0.25, alto * 0.4)
        centro_der = (ancho * 0.75, alto * 0.4)

        # 1. Dibujar LED Izquierdo
        self._dibujar_led(
            painter,
            centro_izq[0],
            centro_izq[1],
            radio_led,
            self._nivel_izq,
            "HEMISFERIO\nIZQUIERDO",
            QColor("#3b82f6"),  # Azul
        )

        # 2. Dibujar LED Derecho
        self._dibujar_led(
            painter,
            centro_der[0],
            centro_der[1],
            radio_led,
            self._nivel_der,
            "HEMISFERIO\nDERECHO",
            QColor("#ef4444"),  # Rojo
        )

    def _dibujar_led(self, painter, x, y, r, intensidad, etiqueta, color_base):
        # Fondo del LED (apagado)
        painter.setPen(QPen(QColor("#4b5563"), 2))
        painter.setBrush(QColor("#1f2937"))
        painter.drawEllipse(x - r, y - r, r * 2, r * 2)

        # Brillo / Luz cuando está activo
        if intensidad > 0.05:
            color_activo = QColor(color_base)
            color_activo.setAlphaF(intensidad)

            gradiente = QLinearGradient(x - r, y - r, x + r, y + r)
            gradiente.setColorAt(0, QColor("#ffffff"))
            gradiente.setColorAt(1, color_activo)

            painter.setPen(Qt.NoPen)
            painter.setBrush(gradiente)
            painter.drawEllipse(x - (r - 2), y - (r - 2), (r - 2) * 2, (r - 2) * 2)

        # Etiqueta de texto inferior
        painter.setPen(QColor("#e5e7eb"))
        painter.setFont(QFont("Bahnschrift", 9, QFont.Bold))
        rect_texto = QRectF(x - r - 20, y + r + 5, (r + 20) * 2, 35)
        painter.drawText(rect_texto, Qt.AlignCenter, etiqueta)