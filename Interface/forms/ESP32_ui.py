# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ESP32.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(965, 574)
        Form.setStyleSheet(u"""
            QWidget {
                background-color: rgb(25, 29, 63);
                color: white;
                font-family: Bahnschrift;
                font-size: 14px;
            }

            QLabel {
                color: white;
                background-color: transparent;
                border: none;
            }

            QPushButton {
                min-height: 30px;
                padding: 6px 16px;
                background-color: rgb(86, 82, 145);
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: rgb(105, 100, 175);
            }

            QPushButton:pressed {
                background-color: rgb(65, 61, 120);
            }

            QPushButton:disabled {
                background-color: rgb(70, 68, 95);
                color: rgb(160, 160, 160);
            }

            QCheckBox {
                color: white;
                spacing: 6px;
            }

            QLineEdit, QTextEdit, QPlainTextEdit {
                background-color: rgb(246, 245, 244);
                color: rgb(36, 31, 49);
                border: none;
                border-radius: 10px;
                padding: 6px;
            }

            QFrame, QWidget#widget {
                background-color: rgb(25, 29, 63);
                border: none;
                border-radius: 20px;
            }

            QLCDNumber {
                color: white;
                background-color: rgb(40, 36, 76);
                border: none;
                border-radius: 10px;
            }
        """)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"""
            QWidget#widget {
                background-color: rgb(25, 29, 63);
                border: none;
                border-radius: 20px;
            }
        """)
        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Serial Data de ESP32</span></p></body></html>", None))
    # retranslateUi

