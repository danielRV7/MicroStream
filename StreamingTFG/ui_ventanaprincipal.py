# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipal.ui'
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


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(820, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaPrincipal.sizePolicy().hasHeightForWidth())
        VentanaPrincipal.setSizePolicy(sizePolicy)
        VentanaPrincipal.setMinimumSize(QSize(820, 540))
        VentanaPrincipal.setMaximumSize(QSize(820, 540))
        font = QFont()
        font.setFamily(u".AppleSystemUIFont")
        VentanaPrincipal.setFont(font)
        VentanaPrincipal.setAutoFillBackground(False)
        VentanaPrincipal.setStyleSheet(u"")
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-image: url(:/resources/Imagenes/fondoMain.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(179, 179, 179);\n"
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
        self.botonAjustes = QPushButton(self.centralwidget)
        self.botonAjustes.setObjectName(u"botonAjustes")
        self.botonAjustes.setGeometry(QRect(30, 310, 80, 31))
        self.botonAjustes.setAutoDefault(False)
        self.botonAjustes.setFlat(False)
        self.botonIniciar = QPushButton(self.centralwidget)
        self.botonIniciar.setObjectName(u"botonIniciar")
        self.botonIniciar.setGeometry(QRect(390, 370, 80, 31))
        self.botonIniciar.setAutoFillBackground(False)
        self.botonIniciar.setAutoDefault(False)
        self.botonIniciar.setFlat(False)
        self.selectorPelicula = QComboBox(self.centralwidget)
        self.selectorPelicula.addItem("")
        self.selectorPelicula.addItem("")
        self.selectorPelicula.setObjectName(u"selectorPelicula")
        self.selectorPelicula.setGeometry(QRect(302, 260, 294, 24))
        self.selectorPelicula.setMinimumSize(QSize(0, 1))
        self.selectorPelicula.setEditable(False)
        self.elegirVideos = QRadioButton(self.centralwidget)
        self.elegirVideos.setObjectName(u"elegirVideos")
        self.elegirVideos.setGeometry(QRect(270, 260, 100, 22))
        self.elegirVideos.setChecked(False)
        self.elegirUrl = QRadioButton(self.centralwidget)
        self.elegirUrl.setObjectName(u"elegirUrl")
        self.elegirUrl.setGeometry(QRect(270, 310, 100, 22))
        self.campoUrl = QLineEdit(self.centralwidget)
        self.campoUrl.setObjectName(u"campoUrl")
        self.campoUrl.setGeometry(QRect(310, 310, 281, 24))
        self.mensaje = QLabel(self.centralwidget)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setEnabled(True)
        self.mensaje.setGeometry(QRect(320, 440, 241, 22))
        VentanaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaPrincipal)

        self.botonAjustes.setDefault(False)
        self.botonIniciar.setDefault(False)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"MicroStream", None))
        self.botonAjustes.setText(QCoreApplication.translate("VentanaPrincipal", u"Ajustes", None))
        self.botonIniciar.setText(QCoreApplication.translate("VentanaPrincipal", u"GO!", None))
        self.selectorPelicula.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Dragon Adventure", None))
        self.selectorPelicula.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Big Buck Bunny", None))

        self.elegirVideos.setText("")
        self.elegirUrl.setText("")
        self.campoUrl.setText(QCoreApplication.translate("VentanaPrincipal", u"Introduce la URL de un fichero .mpd", None))
        self.mensaje.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:14pt; color:#fc0107;\">Por favor, selecciona una opcion.</span></p></body></html>", None))
    # retranslateUi

