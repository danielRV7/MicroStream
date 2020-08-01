import sys,gi

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui 

from PySide2.QtWidgets import QMainWindow
from ui_ventanaajustes import Ui_VentanaAjustes

from images import *


class ajustes(QMainWindow):
    def __init__(self,app):
        QMainWindow.__init__(self)
        self.ui = Ui_VentanaAjustes()
        self.ui.setupUi(self)
        self.show()
        self.ui.botonSave.clicked.connect(self.guardarAjustes)
        self.ui.botonCancelar.clicked.connect(self.cancelarAjustes)

        # Establecimiento de valores por defecto.
        self.anchura = 1920
        self.altura = 1080
        self.framerate = 60
        self.bitrate = 5
        self.info = False

    def guardarAjustes(self):
        # Son los valores máximos que tendrá la aplicación
        self.anchura = self.ui.campoAnchura.text()
        self.altura = self.ui.campoAltura.text()
        self.framerate = self.ui.campoFramerate.text()
        self.bitrate = self.ui.campoBitrate.text()
        self.info = self.ui.activarInfo.isChecked()
        self.close()

    def cancelarAjustes(self):
        self.close()
