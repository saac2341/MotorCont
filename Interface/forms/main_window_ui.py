# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

import forms.recurces_rc as recurces_rc 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1019, 538)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(40, 36, 76);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.opcionControl = QFrame(self.centralwidget)
        self.opcionControl.setObjectName(u"opcionControl")
        self.opcionControl.setMaximumSize(QSize(120, 16777215))
        self.opcionControl.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 29, 63);\n"
"}")
        self.opcionControl.setFrameShape(QFrame.Shape.StyledPanel)
        self.opcionControl.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.opcionControl)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 2, 6, 6)
        self.label = QLabel(self.opcionControl)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setTabletTracking(False)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(40, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btnFiltro = QPushButton(self.opcionControl)
        self.btnFiltro.setObjectName(u"btnFiltro")
        font1 = QFont()
        self.btnFiltro.setFont(font1)
        self.btnFiltro.setStyleSheet(u"/* Estado Normal */\n"
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
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/icons8-loop-24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFiltro.setIcon(icon)
        self.btnFiltro.setFlat(True)

        self.verticalLayout_2.addWidget(self.btnFiltro)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.btnImpulse = QPushButton(self.opcionControl)
        self.btnImpulse.setObjectName(u"btnImpulse")
        self.btnImpulse.setStyleSheet(u"/* Estado Normal */\n"
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
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/icons8-lightning-arrow-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnImpulse.setIcon(icon1)
        self.btnImpulse.setFlat(True)

        self.verticalLayout_2.addWidget(self.btnImpulse, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.btnESP32 = QPushButton(self.opcionControl)
        self.btnESP32.setObjectName(u"btnESP32")
        self.btnESP32.setStyleSheet(u"/* Estado Normal */\n"
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
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/icons8-usb-connector-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnESP32.setIcon(icon2)
        self.btnESP32.setFlat(True)

        self.verticalLayout_2.addWidget(self.btnESP32)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.default_2 = QPushButton(self.opcionControl)
        self.default_2.setObjectName(u"default_2")
        self.default_2.setStyleSheet(u"/* Estado Normal */\n"
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
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")

        self.verticalLayout_2.addWidget(self.default_2)

        self.verticalSpacer = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnDesconec = QPushButton(self.opcionControl)
        self.btnDesconec.setObjectName(u"btnDesconec")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.btnDesconec.setFont(font2)
        self.btnDesconec.setStyleSheet(u"/* Estado Normal */\n"
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
        self.btnDesconec.setAutoDefault(True)
        self.btnDesconec.setFlat(True)

        self.verticalLayout_2.addWidget(self.btnDesconec, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.opcionControl)

        self.frame_default = QFrame(self.centralwidget)
        self.frame_default.setObjectName(u"frame_default")
        self.frame_default.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_default.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_default)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_ip = QFrame(self.frame_default)
        self.frame_ip.setObjectName(u"frame_ip")
        self.frame_ip.setMaximumSize(QSize(16777215, 50))
        self.frame_ip.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(25, 29, 63);\n"
"	border-radius: 20px;\n"
"	border: 2px solid #DB7829;\n"
"}")
        self.frame_ip.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ip.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_ip)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_ip)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"MesloLGLDZ Nerd Font Propo"])
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u".QLabel{\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"	color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.frame_ip)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.frame_ip)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(36, 31, 49);\n"
"background-color: rgb(246, 245, 244);")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.pushButton_5 = QPushButton(self.frame_ip)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"/* Estado Normal */\n"
"QPushButton {\n"
"    background-color: rgba(191, 64, 64, 0);\n"
"    color: #ffffff;\n"
"    border: none;\n"
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
"    background-color: rgb(38, 162, 105);\n"
"}\n"
"\n"
"/* Estado Deshabilitado (Disabled) */\n"
"QPushButton:disabled {\n"
"    background-color: #9ca3af;\n"
"    color: #e5e7eb;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/tocar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame_ip)

        self.frame_wiget = QFrame(self.frame_default)
        self.frame_wiget.setObjectName(u"frame_wiget")
        self.frame_wiget.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_wiget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_wiget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pagWidget = QStackedWidget(self.frame_wiget)
        self.pagWidget.setObjectName(u"pagWidget")
        font4 = QFont()
        font4.setFamilies([u"Candara"])
        font4.setBold(False)
        self.pagWidget.setFont(font4)
        self.page_Senal = QWidget()
        self.page_Senal.setObjectName(u"page_Senal")
        self.pagWidget.addWidget(self.page_Senal)
        self.page_Filtt = QWidget()
        self.page_Filtt.setObjectName(u"page_Filtt")
        self.pagWidget.addWidget(self.page_Filtt)
        self.page_Impulse = QWidget()
        self.page_Impulse.setObjectName(u"page_Impulse")
        self.pagWidget.addWidget(self.page_Impulse)
        self.page_esp = QWidget()
        self.page_esp.setObjectName(u"page_esp")
        self.pagWidget.addWidget(self.page_esp)

        self.horizontalLayout_3.addWidget(self.pagWidget)


        self.verticalLayout.addWidget(self.frame_wiget)


        self.horizontalLayout.addWidget(self.frame_default)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pagWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/prefijoNuevo/icons8-brain-64.png\"/></p></body></html>", None))
        self.btnFiltro.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.btnImpulse.setText(QCoreApplication.translate("MainWindow", u"Impulse", None))
        self.btnESP32.setText(QCoreApplication.translate("MainWindow", u"ESP32", None))
        self.default_2.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.btnDesconec.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Conectar direcci\u00f3n IP</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
    # retranslateUi

