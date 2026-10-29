# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filtrosOMfVsP.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(907, 657)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(40, 36, 76);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.filtro_ops = QFrame(Form)
        self.filtro_ops.setObjectName(u"filtro_ops")
        self.filtro_ops.setMaximumSize(QSize(16777215, 80))
        self.filtro_ops.setFrameShape(QFrame.Shape.StyledPanel)
        self.filtro_ops.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.filtro_ops)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.filtro_ops)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setBold(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"/* Estado Normal */\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"/* Estado Normal */\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.filtro_ops)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, -1, -1)
        self.radioButton = QRadioButton(self.frame_8)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"/* Estado base del texto y contenedor */\n"
"QRadioButton {\n"
"    color: #e5e7eb;\n"
"    font-size: 14px;\n"
"    spacing: 6px; /* Espacio entre el c\u00edrculo y el texto */\n"
"}\n"
"\n"
"/* Tama\u00f1o del indicador (el c\u00edrculo) */\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 7px; /* Mitad del ancho/alto + borde para que sea circular */\n"
"    border: 2px solid #6b7280;\n"
"    background-color: #1f2937;\n"
"}\n"
"\n"
"/* Hover sobre el c\u00edrculo cuando NO est\u00e1 seleccionado */\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color: #38bdf8;\n"
"}\n"
"\n"
"/* Estado SELECCIONADO (Checked) */\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #38bdf8;\n"
"    background-color: #38bdf8;\n"
"    /* En QSS puro creamos el punto central con una imagen o con m\u00e1rgenes/relleno */\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_8)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"/* Estado base del texto y contenedor */\n"
"QRadioButton {\n"
"    color: #e5e7eb;\n"
"    font-size: 14px;\n"
"    spacing: 6px; /* Espacio entre el c\u00edrculo y el texto */\n"
"}\n"
"\n"
"/* Tama\u00f1o del indicador (el c\u00edrculo) */\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 7px; /* Mitad del ancho/alto + borde para que sea circular */\n"
"    border: 2px solid #6b7280;\n"
"    background-color: #1f2937;\n"
"}\n"
"\n"
"/* Hover sobre el c\u00edrculo cuando NO est\u00e1 seleccionado */\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color: #38bdf8;\n"
"}\n"
"\n"
"/* Estado SELECCIONADO (Checked) */\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #38bdf8;\n"
"    background-color: #38bdf8;\n"
"    /* En QSS puro creamos el punto central con una imagen o con m\u00e1rgenes/relleno */\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_8)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"/* Estado base del texto y contenedor */\n"
"QRadioButton {\n"
"    color: #e5e7eb;\n"
"    font-size: 14px;\n"
"    spacing: 6px; /* Espacio entre el c\u00edrculo y el texto */\n"
"}\n"
"\n"
"/* Tama\u00f1o del indicador (el c\u00edrculo) */\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 7px; /* Mitad del ancho/alto + borde para que sea circular */\n"
"    border: 2px solid #6b7280;\n"
"    background-color: #1f2937;\n"
"}\n"
"\n"
"/* Hover sobre el c\u00edrculo cuando NO est\u00e1 seleccionado */\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color: #38bdf8;\n"
"}\n"
"\n"
"/* Estado SELECCIONADO (Checked) */\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #38bdf8;\n"
"    background-color: #38bdf8;\n"
"    /* En QSS puro creamos el punto central con una imagen o con m\u00e1rgenes/relleno */\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.spinBox = QSpinBox(self.frame_8)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);")

        self.horizontalLayout.addWidget(self.spinBox)

        self.textEdit = QTextEdit(self.frame_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.filtro_ops)

        self.filtro_grafs = QFrame(Form)
        self.filtro_grafs.setObjectName(u"filtro_grafs")
        self.filtro_grafs.setFrameShape(QFrame.Shape.StyledPanel)
        self.filtro_grafs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.filtro_grafs)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.filtro_grafs)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 25))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white \n"
"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(757, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u".QWidget{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 30px;\n"
"}")

        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.filtro_grafs)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 25))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(740, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u".QWidget{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 30px;\n"
"}")

        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.filtro_grafs)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Editor de filtros de la muestra", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Exportar CVS", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Exportar JSON", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Pasa bajas", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Pasa Altas", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Combinado", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Antes de los filtros", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Despues de los filtros", None))
    # retranslateUi

