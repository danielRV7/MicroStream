# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaGraficas.ui'
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


class Ui_VentanaGraficas(object):
    def setupUi(self, VentanaGraficas):
        if not VentanaGraficas.objectName():
            VentanaGraficas.setObjectName(u"VentanaGraficas")
        VentanaGraficas.resize(1024, 700)
        VentanaGraficas.setMinimumSize(QSize(1024, 700))
        VentanaGraficas.setMaximumSize(QSize(1024, 700))
        VentanaGraficas.setStyleSheet(u"background-image: url(:/resources/Imagenes/fondoGraficas.png);")
        self.centralwidget = QWidget(VentanaGraficas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 20, 801, 531))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(350, 570, 321, 101))
        self.listView.setStyleSheet(u"color: rgb(0, 0, 0);")
        VentanaGraficas.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaGraficas)

        QMetaObject.connectSlotsByName(VentanaGraficas)
    # setupUi

    def retranslateUi(self, VentanaGraficas):
        VentanaGraficas.setWindowTitle(QCoreApplication.translate("VentanaGraficas", u"Gr\u00e1ficas", None))
    # retranslateUi

