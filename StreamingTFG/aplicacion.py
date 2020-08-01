import sys,gi

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

from stream import reproductor
from ajustes import ajustes

from PySide2.QtWidgets import QMainWindow
from ui_ventanaprincipal import Ui_VentanaPrincipal

from images import *

gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')


class StreamingTFG(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.ui.mensaje.setVisible(0)

        self.ui.botonAjustes.clicked.connect(self.abrirAjustes)
        self.ui.botonIniciar.clicked.connect(self.abrirReproductor)

        self.selector = self.ui.selectorPelicula.currentIndex()
        self.ui.selectorPelicula.activated.connect(self.guardarValorSelector)

        self.url = ""
        self.ajustes = 0

    def urlPelicula(self):
        if self.selector == 0:
            self.url = "http://localhost/dragon/dragon.mpd"
        else:
            self.url = "http://localhost/bunny/bunny.mpd"

    def guardarValorSelector(self, index):
        self.selector = self.ui.selectorPelicula.currentIndex()

    def abrirAjustes(self):
        self.ajustes = ajustes(self)

    def abrirReproductor(self):
        if self.ui.elegirVideos.isChecked():
            self.urlPelicula()
            self.reproductor = reproductor(self.url, self.ajustes)
        elif self.ui.elegirUrl.isChecked():
            self.url = self.ui.campoUrl.text()
            self.reproductor = reproductor(self.url, self.ajustes)
        else:
            self.ui.mensaje.setVisible(1)


