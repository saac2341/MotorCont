# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edgeImpulse.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from kled import KLed

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 632)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(40, 36, 76);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_data = QFrame(Form)
        self.frame_data.setObjectName(u"frame_data")
        self.frame_data.setMaximumSize(QSize(480, 16777215))
        self.frame_data.setStyleSheet(u"border:none")
        self.frame_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_data)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_data)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;\n"
"")

        self.verticalLayout_3.addWidget(self.label_2)

        self.line_Token = QLineEdit(self.frame_data)
        self.line_Token.setObjectName(u"line_Token")
        self.line_Token.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);\n"
"border-radius: 10px;")

        self.verticalLayout_3.addWidget(self.line_Token)

        self.list_Archive = QListWidget(self.frame_data)
        self.list_Archive.setObjectName(u"list_Archive")
        self.list_Archive.setStyleSheet(u".QListWidget{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 30px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.list_Archive)

        self.table_archive = QTableWidget(self.frame_data)
        self.table_archive.setObjectName(u"table_archive")
        self.table_archive.setStyleSheet(u".QTableWidget{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 30px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.table_archive)


        self.horizontalLayout.addWidget(self.frame_data)

        self.frame_opts = QFrame(Form)
        self.frame_opts.setObjectName(u"frame_opts")
        self.frame_opts.setMaximumSize(QSize(125, 16777215))
        self.frame_opts.setStyleSheet(u"border: none;\n"
"")
        self.frame_opts.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_opts.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_opts)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame_opts)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.frame_4 = QFrame(self.frame_opts)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.kled_ok = KLed(self.frame_4)
        self.kled_ok.setObjectName(u"kled_ok")
        self.kled_ok.setLook(KLed.Look.Flat)

        self.horizontalLayout_2.addWidget(self.kled_ok, 0, Qt.AlignmentFlag.AlignHCenter)

        self.kled_neutral = KLed(self.frame_4)
        self.kled_neutral.setObjectName(u"kled_neutral")
        self.kled_neutral.setLook(KLed.Look.Flat)
        self.kled_neutral.setColor(QColor(248, 228, 92))

        self.horizontalLayout_2.addWidget(self.kled_neutral, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.kled_process = KLed(self.frame_4)
        self.kled_process.setObjectName(u"kled_process")
        self.kled_process.setLook(KLed.Look.Flat)
        self.kled_process.setColor(QColor(237, 51, 59))

        self.horizontalLayout_2.addWidget(self.kled_process, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.push_upinf = QPushButton(self.frame_opts)
        self.push_upinf.setObjectName(u"push_upinf")
        self.push_upinf.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(255, 120, 0);\n"
"    border-radius: 6px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"/* Al pasar el cursor por encima (Hover) */\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* Al presionar/hacer click (Pressed) */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout.addWidget(self.push_upinf)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.push_reboot = QPushButton(self.frame_opts)
        self.push_reboot.setObjectName(u"push_reboot")
        self.push_reboot.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(255, 120, 0);\n"
"    border-radius: 6px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"/* Al pasar el cursor por encima (Hover) */\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* Al presionar/hacer click (Pressed) */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout.addWidget(self.push_reboot)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.push_anals = QPushButton(self.frame_opts)
        self.push_anals.setObjectName(u"push_anals")
        self.push_anals.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(255, 120, 0);\n"
"    border-radius: 6px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"/* Al pasar el cursor por encima (Hover) */\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* Al presionar/hacer click (Pressed) */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout.addWidget(self.push_anals)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.push_connect = QPushButton(self.frame_opts)
        self.push_connect.setObjectName(u"push_connect")
        self.push_connect.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(255, 120, 0);\n"
"    border-radius: 6px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"/* Al pasar el cursor por encima (Hover) */\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* Al presionar/hacer click (Pressed) */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout.addWidget(self.push_connect)

        self.verticalSpacer = QSpacerItem(20, 185, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.push_cancel = QPushButton(self.frame_opts)
        self.push_cancel.setObjectName(u"push_cancel")
        self.push_cancel.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgb(246, 97, 81);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgb(255, 120, 0);\n"
"    border-radius: 6px;\n"
"    padding: 6px 18px;\n"
"}\n"
"\n"
"/* Al pasar el cursor por encima (Hover) */\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* Al presionar/hacer click (Pressed) */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(237, 51, 59);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout.addWidget(self.push_cancel)


        self.horizontalLayout.addWidget(self.frame_opts)

        self.frame_edge = QFrame(Form)
        self.frame_edge.setObjectName(u"frame_edge")
        self.frame_edge.setStyleSheet(u"border: none;")
        self.frame_edge.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_edge.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_edge)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_edge)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"color: white;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.webpageImpulse = QWebEngineView(self.frame_edge)
        self.webpageImpulse.setObjectName(u"webpageImpulse")
        self.webpageImpulse.setStyleSheet(u"QWebEngineView {\n"
"    border: 2px solid #374151;\n"
"    border-radius: 10px;\n"
"    background-color: #111827; /* Se muestra mientras carga la p\u00e1gina */\n"
"}")
        self.webpageImpulse.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webpageImpulse)

        self.label_4 = QLabel(self.frame_edge)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"color: white;\n"
"")

        self.verticalLayout_2.addWidget(self.label_4)

        self.widget_Serial = QWidget(self.frame_edge)
        self.widget_Serial.setObjectName(u"widget_Serial")
        self.widget_Serial.setStyleSheet(u".QWidget{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 30px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_Serial)


        self.horizontalLayout.addWidget(self.frame_edge)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Agregar Token de conexi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edge Impulse", None))
        self.push_upinf.setText(QCoreApplication.translate("Form", u"Subir Archivo", None))
        self.push_reboot.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.push_anals.setText(QCoreApplication.translate("Form", u"Analizar", None))
        self.push_connect.setText(QCoreApplication.translate("Form", u"Conectar", None))
        self.push_cancel.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Visualizar edge terminal", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Pagina Web", None))
    # retranslateUi

