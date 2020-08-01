# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaAjustes.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_VentanaAjustes(object):
    def setupUi(self, VentanaAjustes):
        if not VentanaAjustes.objectName():
            VentanaAjustes.setObjectName(u"VentanaAjustes")
        VentanaAjustes.resize(820, 540)
        VentanaAjustes.setMinimumSize(QSize(820, 540))
        VentanaAjustes.setMaximumSize(QSize(820, 540))
        self.centralwidget = QWidget(VentanaAjustes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-image: url(:/resources/Imagenes/fondoAjustes.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(153, 153, 153);\n"
"border-radius:15px;\n"
"border:1px solid;\n"
"border-color: rgb(102, 102, 102);\n"
"color:#ffffff;\n"
"font-size:13px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(16, 128, 128, 240);\n"
"}")
        self.botonSave = QPushButton(self.centralwidget)
        self.botonSave.setObjectName(u"botonSave")
        self.botonSave.setGeometry(QRect(570, 480, 80, 31))
        self.botonCancelar = QPushButton(self.centralwidget)
        self.botonCancelar.setObjectName(u"botonCancelar")
        self.botonCancelar.setGeometry(QRect(680, 480, 80, 31))
        self.AnchMax = QLabel(self.centralwidget)
        self.AnchMax.setObjectName(u"AnchMax")
        self.AnchMax.setGeometry(QRect(230, 130, 141, 16))
        self.AnchMax.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.campoAnchura = QLineEdit(self.centralwidget)
        self.campoAnchura.setObjectName(u"campoAnchura")
        self.campoAnchura.setGeometry(QRect(420, 130, 113, 24))
        self.AltMax = QLabel(self.centralwidget)
        self.AltMax.setObjectName(u"AltMax")
        self.AltMax.setGeometry(QRect(230, 200, 141, 16))
        self.AltMax.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.campoAltura = QLineEdit(self.centralwidget)
        self.campoAltura.setObjectName(u"campoAltura")
        self.campoAltura.setGeometry(QRect(420, 200, 113, 24))
        self.framerate = QLabel(self.centralwidget)
        self.framerate.setObjectName(u"framerate")
        self.framerate.setGeometry(QRect(230, 270, 141, 16))
        self.framerate.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.bitrate = QLabel(self.centralwidget)
        self.bitrate.setObjectName(u"bitrate")
        self.bitrate.setGeometry(QRect(230, 340, 141, 16))
        self.bitrate.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.campoFramerate = QLineEdit(self.centralwidget)
        self.campoFramerate.setObjectName(u"campoFramerate")
        self.campoFramerate.setGeometry(QRect(420, 270, 113, 24))
        self.campoBitrate = QLineEdit(self.centralwidget)
        self.campoBitrate.setObjectName(u"campoBitrate")
        self.campoBitrate.setGeometry(QRect(420, 340, 113, 24))
        self.activarInfo = QCheckBox(self.centralwidget)
        self.activarInfo.setObjectName(u"activarInfo")
        self.activarInfo.setGeometry(QRect(230, 405, 441, 22))
        self.activarInfo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dibujoAjustes = QLabel(self.centralwidget)
        self.dibujoAjustes.setObjectName(u"dibujoAjustes")
        self.dibujoAjustes.setGeometry(QRect(340, 20, 131, 51))
        font = QFont()
        font.setFamily(u"Gill Sans")
        font.setPointSize(37)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dibujoAjustes.setFont(font)
        self.dibujoAjustes.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dibujoTiempo = QLabel(self.centralwidget)
        self.dibujoTiempo.setObjectName(u"dibujoTiempo")
        self.dibujoTiempo.setGeometry(QRect(560, 334, 41, 31))
        self.dibujoTiempo.setStyleSheet(u"image: url(:/resources/Imagenes/cronometro.png);")
        self.dibujoAltura = QLabel(self.centralwidget)
        self.dibujoAltura.setObjectName(u"dibujoAltura")
        self.dibujoAltura.setGeometry(QRect(554, 190, 51, 41))
        self.dibujoAltura.setStyleSheet(u"image: url(:/resources/Imagenes/alto.png);")
        self.dibujoFPS = QLabel(self.centralwidget)
        self.dibujoFPS.setObjectName(u"dibujoFPS")
        self.dibujoFPS.setGeometry(QRect(560, 270, 41, 31))
        self.dibujoFPS.setStyleSheet(u"image: url(:/resources/Imagenes/fps.png);")
        self.dibujoAnchura = QLabel(self.centralwidget)
        self.dibujoAnchura.setObjectName(u"dibujoAnchura")
        self.dibujoAnchura.setGeometry(QRect(560, 130, 41, 31))
        self.dibujoAnchura.setStyleSheet(u"image: url(:/resources/Imagenes/ancho.png);")
        VentanaAjustes.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaAjustes)

        QMetaObject.connectSlotsByName(VentanaAjustes)
    # setupUi

    def retranslateUi(self, VentanaAjustes):
        VentanaAjustes.setWindowTitle(QCoreApplication.translate("VentanaAjustes", u"Ajustes", None))
        self.botonSave.setText(QCoreApplication.translate("VentanaAjustes", u"Guardar", None))
        self.botonCancelar.setText(QCoreApplication.translate("VentanaAjustes", u"Cancelar", None))
        self.AnchMax.setText(QCoreApplication.translate("VentanaAjustes", u"Anchura m\u00e1xima (px): ", None))
        self.campoAnchura.setText(QCoreApplication.translate("VentanaAjustes", u"1920", None))
        self.AltMax.setText(QCoreApplication.translate("VentanaAjustes", u"Altura m\u00e1xima (px):", None))
        self.campoAltura.setText(QCoreApplication.translate("VentanaAjustes", u"1080", None))
        self.framerate.setText(QCoreApplication.translate("VentanaAjustes", u"Framerate m\u00e1ximo:", None))
        self.bitrate.setText(QCoreApplication.translate("VentanaAjustes", u"Bitrate m\u00e1ximo (Mbps):", None))
        self.campoFramerate.setText(QCoreApplication.translate("VentanaAjustes", u"60", None))
        self.campoBitrate.setText(QCoreApplication.translate("VentanaAjustes", u"5", None))
        self.activarInfo.setText(QCoreApplication.translate("VentanaAjustes", u"Mostrar informaci\u00f3n de rendimiento del video durante la reproducci\u00f3n", None))
        self.dibujoAjustes.setText(QCoreApplication.translate("VentanaAjustes", u"Ajustes", None))
        self.dibujoTiempo.setText("")
        self.dibujoAltura.setText("")
        self.dibujoFPS.setText("")
        self.dibujoAnchura.setText("")
    # retranslateUi

