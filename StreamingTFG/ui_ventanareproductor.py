# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaReproductor.ui'
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


class Ui_VentanaReproductor(object):
    def setupUi(self, VentanaReproductor):
        if not VentanaReproductor.objectName():
            VentanaReproductor.setObjectName(u"VentanaReproductor")
        VentanaReproductor.resize(1024, 768)
        VentanaReproductor.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(VentanaReproductor)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(153, 153, 153);\n"
"border:1px solid;\n"
"border-color: rgb(102, 102, 102);\n"
"color:#ffffff;\n"
"font-size:13px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(16, 128, 128, 240);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameVideo = QFrame(self.centralwidget)
        self.frameVideo.setObjectName(u"frameVideo")
        self.frameVideo.setFrameShape(QFrame.StyledPanel)
        self.frameVideo.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameVideo)

        self.barraProgreso = QProgressBar(self.centralwidget)
        self.barraProgreso.setObjectName(u"barraProgreso")
        self.barraProgreso.setValue(0)
        self.barraProgreso.setTextVisible(False)

        self.verticalLayout.addWidget(self.barraProgreso)

        self.barraAvanzar = QSlider(self.centralwidget)
        self.barraAvanzar.setObjectName(u"barraAvanzar")
        self.barraAvanzar.setMaximum(100)
        self.barraAvanzar.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.barraAvanzar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonGraficas = QPushButton(self.centralwidget)
        self.botonGraficas.setObjectName(u"botonGraficas")
        self.botonGraficas.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botonGraficas.sizePolicy().hasHeightForWidth())
        self.botonGraficas.setSizePolicy(sizePolicy1)
        self.botonGraficas.setMinimumSize(QSize(0, 0))
        self.botonGraficas.setMaximumSize(QSize(36, 36))
        self.botonGraficas.setStyleSheet(u"image: url(:/resources/Imagenes/graficas.png);")
        self.botonGraficas.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.botonGraficas)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(50, 30))
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label)

        self.barraVolumen = QSlider(self.centralwidget)
        self.barraVolumen.setObjectName(u"barraVolumen")
        self.barraVolumen.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.barraVolumen.sizePolicy().hasHeightForWidth())
        self.barraVolumen.setSizePolicy(sizePolicy2)
        self.barraVolumen.setMinimumSize(QSize(0, 0))
        self.barraVolumen.setMaximumSize(QSize(240, 30))
        self.barraVolumen.setValue(40)
        self.barraVolumen.setOrientation(Qt.Horizontal)
        self.barraVolumen.setTickPosition(QSlider.TicksBelow)
        self.barraVolumen.setTickInterval(20)

        self.horizontalLayout.addWidget(self.barraVolumen)

        self.espacio = QSpacerItem(350, 30, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.espacio)

        self.botonPlay = QPushButton(self.centralwidget)
        self.botonPlay.setObjectName(u"botonPlay")
        sizePolicy2.setHeightForWidth(self.botonPlay.sizePolicy().hasHeightForWidth())
        self.botonPlay.setSizePolicy(sizePolicy2)
        self.botonPlay.setMaximumSize(QSize(140, 20))

        self.horizontalLayout.addWidget(self.botonPlay)

        self.botonStop = QPushButton(self.centralwidget)
        self.botonStop.setObjectName(u"botonStop")
        sizePolicy2.setHeightForWidth(self.botonStop.sizePolicy().hasHeightForWidth())
        self.botonStop.setSizePolicy(sizePolicy2)
        self.botonStop.setMaximumSize(QSize(140, 20))

        self.horizontalLayout.addWidget(self.botonStop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        VentanaReproductor.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaReproductor)
        self.barraAvanzar.valueChanged.connect(self.barraProgreso.setValue)

        QMetaObject.connectSlotsByName(VentanaReproductor)
    # setupUi

    def retranslateUi(self, VentanaReproductor):
        VentanaReproductor.setWindowTitle(QCoreApplication.translate("VentanaReproductor", u"Reproductor", None))
        self.botonGraficas.setText("")
        self.label.setText(QCoreApplication.translate("VentanaReproductor", u"Volume", None))
#if QT_CONFIG(accessibility)
        self.barraVolumen.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.barraVolumen.setAccessibleDescription(QCoreApplication.translate("VentanaReproductor", u"hola", None))
#endif // QT_CONFIG(accessibility)
        self.botonPlay.setText(QCoreApplication.translate("VentanaReproductor", u"Play", None))
        self.botonStop.setText(QCoreApplication.translate("VentanaReproductor", u"Stop", None))
    # retranslateUi

