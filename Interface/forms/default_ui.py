# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'default.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(902, 609)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_all = QFrame(Form)
        self.frame_all.setObjectName(u"frame_all")
        self.frame_all.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 29, 63);\n"
"}")
        self.frame_all.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_all.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_all)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_ops = QFrame(self.frame_all)
        self.frame_ops.setObjectName(u"frame_ops")
        self.frame_ops.setMaximumSize(QSize(16777215, 40))
        self.frame_ops.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ops.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ops)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_ops)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_3 = QPushButton(self.frame_ops)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_ops)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.checkBox = QCheckBox(self.frame_ops)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: white;")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.frame_ops)

        self.frame_monitor = QFrame(self.frame_all)
        self.frame_monitor.setObjectName(u"frame_monitor")
        self.frame_monitor.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_monitor.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_monitor)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_graf_2 = QFrame(self.frame_monitor)
        self.frame_graf_2.setObjectName(u"frame_graf_2")
        self.frame_graf_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_graf_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_graf_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_7 = QFrame(self.frame_graf_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 20))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_gono = QFrame(self.frame_graf_2)
        self.frame_gono.setObjectName(u"frame_gono")
        self.frame_gono.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gono.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_gono)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_Gono = QWidget(self.frame_gono)
        self.widget_Gono.setObjectName(u"widget_Gono")

        self.verticalLayout_6.addWidget(self.widget_Gono)

        self.lcdIndicador = QLCDNumber(self.frame_gono)
        self.lcdIndicador.setObjectName(u"lcdIndicador")
        self.lcdIndicador.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_6.addWidget(self.lcdIndicador)


        self.verticalLayout_3.addWidget(self.frame_gono)


        self.horizontalLayout_2.addWidget(self.frame_graf_2)

        self.frame_cereb = QFrame(self.frame_monitor)
        self.frame_cereb.setObjectName(u"frame_cereb")
        self.frame_cereb.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cereb.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_cereb)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame_9 = QFrame(self.frame_cereb)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 20))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.widget_3 = QWidget(self.frame_cereb)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_4.addWidget(self.widget_3)

        self.label_act = QLabel(self.frame_cereb)
        self.label_act.setObjectName(u"label_act")
        self.label_act.setMaximumSize(QSize(16777215, 30))
        self.label_act.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);\n"
"border-radius: 10px;")

        self.verticalLayout_4.addWidget(self.label_act)


        self.horizontalLayout_2.addWidget(self.frame_cereb)


        self.verticalLayout.addWidget(self.frame_monitor)

        self.frame_graf = QFrame(self.frame_all)
        self.frame_graf.setObjectName(u"frame_graf")
        self.frame_graf.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_graf.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_graf)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_lambel = QFrame(self.frame_graf)
        self.frame_lambel.setObjectName(u"frame_lambel")
        self.frame_lambel.setMaximumSize(QSize(16777215, 20))
        self.frame_lambel.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lambel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_lambel)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(348, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.frame_lambel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(191, 0))
        self.label_4.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(347, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.frame_lambel)

        self.widget_graf = QWidget(self.frame_graf)
        self.widget_graf.setObjectName(u"widget_graf")
        self.widget_graf.setStyleSheet(u".QWhite{\n"
"	background-color: ;\n"
"	color: rgb(40, 36, 76);\n"
"	border-radius: 20px;	\n"
"}")

        self.verticalLayout_5.addWidget(self.widget_graf)


        self.verticalLayout.addWidget(self.frame_graf)


        self.verticalLayout_2.addWidget(self.frame_all)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tomar Muestras ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Capturar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Detener", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Escalar grafica", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Gonometro </span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Actividad cerebral", None))
        self.label_act.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Grafica respecto al tiempo", None))
    # retranslateUi

