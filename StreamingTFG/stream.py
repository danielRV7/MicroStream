import sys, gi, threading, time, re
import urllib.request
import xml.etree.ElementTree as ET

from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import SIGNAL, Qt, QDateTime
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter

from ui_ventanareproductor import Ui_VentanaReproductor

gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')

from gi.repository import Gst, GstVideo, GLib
from graficas import graficas
from ajustes import ajustes


class stream:
    def __init__(self, windowId, url, arrayAjustes):

        self.windowId = windowId
        self.url = url
        self.arrayAjustes = arrayAjustes

        self.current_representation = ''

        # Creacion del pipeline.
        Gst.init(None)
        self.crearPipeline(self.url)

    def crearPipeline(self, url):

        # Pipeline
        self.pipeline = Gst.Pipeline.new("pipeline")

        # Fuente HTTP
        self.http = Gst.ElementFactory.make('souphttpsrc')
        self.http.set_property('location', url)

        # Demultiplexor DASH
        self.dashdemux = Gst.ElementFactory.make('dashdemux')

        if self.arrayAjustes:           
            if self.arrayAjustes[0]:
                self.dashdemux.set_property('max-video-width', int(self.arrayAjustes[0]))
            if self.arrayAjustes[1]:
                self.dashdemux.set_property('max-video-height', int(self.arrayAjustes[1]))
            if self.arrayAjustes[2]:
                self.dashdemux.set_property('max-video-framerate', Gst.Fraction(int(self.arrayAjustes[2]), 1))
            if self.arrayAjustes[3]:
                self.dashdemux.set_property('max-bitrate', int(int(self.arrayAjustes[3])*1.0e6))
        #else:
            #self.dashdemux.set_property('max-video-width', 3840)
            #self.dashdemux.set_property('max-video-height', 2160)
            #self.dashdemux.set_property('max-video-framerate', Gst.Fraction(60, 1))
            #self.dashdemux.set_property('max-bitrate', int(15*1.0e6))

        # Cola para almacenar trozos de video.
        self.cola_video = Gst.ElementFactory.make('queue')
        self.qtdemux_video = Gst.ElementFactory.make('qtdemux')
        self.h265parse = Gst.ElementFactory.make('h265parse')
        self.h265dec = Gst.ElementFactory.make('avdec_h265')
        self.videoconvert = Gst.ElementFactory.make('videoconvert')
        self.videoscale = Gst.ElementFactory.make('videoscale')

        # Visualizador del video con overlay.
        self.display = Gst.ElementFactory.make('fpsdisplaysink')
        self.glimagesink = Gst.ElementFactory.make('glimagesink')
        self.display.set_property('video-sink', self.glimagesink)
        self.display.set_property('fps-update-interval', 100)

        if self.arrayAjustes and self.arrayAjustes[4]:
            self.display.set_property('text-overlay', True)
        else:
            self.display.set_property('text-overlay', False)

        # Cola para almacenar trozos de audio.
        self.cola_audio = Gst.ElementFactory.make('queue')
        self.qtdemux_audio = Gst.ElementFactory.make('qtdemux')
        self.aacparse = Gst.ElementFactory.make('aacparse')
        self.aacdec = Gst.ElementFactory.make('avdec_aac')
        self.audioconvert = Gst.ElementFactory.make('audioconvert')
        self.audioresample = Gst.ElementFactory.make('audioresample')
        self.volume = Gst.ElementFactory.make('volume')
        self.audiosink = Gst.ElementFactory.make('autoaudiosink')

        # Se añaden los componentes.
        self.pipeline.add(self.http)
        self.pipeline.add(self.dashdemux)
        self.pipeline.add(self.cola_video)
        self.pipeline.add(self.qtdemux_video)
        self.pipeline.add(self.h265parse)
        self.pipeline.add(self.h265dec)
        self.pipeline.add(self.videoconvert)
        self.pipeline.add(self.videoscale)
        self.pipeline.add(self.display)
        self.pipeline.add(self.cola_audio)
        self.pipeline.add(self.qtdemux_audio)
        self.pipeline.add(self.aacparse)
        self.pipeline.add(self.aacdec)
        self.pipeline.add(self.audioconvert)
        self.pipeline.add(self.audioresample)
        self.pipeline.add(self.volume)
        self.pipeline.add(self.audiosink)

        # Se enlazan los componentes que ya se pueden conectar.
        self.http.link(self.dashdemux)
        self.cola_video.link(self.qtdemux_video)
        self.h265parse.link(self.h265dec)
        self.h265dec.link(self.videoconvert)
        self.videoconvert.link(self.videoscale)
        self.videoscale.link(self.display)

        self.cola_audio.link(self.qtdemux_audio)
        self.aacparse.link(self.aacdec)
        self.aacdec.link(self.audioconvert)
        self.audioconvert.link(self.audioresample)
        self.audioresample.link(self.volume)
        self.volume.link(self.audiosink)

        self.dashdemux.connect('pad-added', self.on_dash_pad_added)
        self.qtdemux_video.connect('pad-added', self.on_qt_pad_added, self.h265parse)
        self.qtdemux_audio.connect('pad-added', self.on_qt_pad_added, self.aacparse)

        # Eventos del pipeline.
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        self.bus.connect('sync-message::element', self.on_sync_message)

        self.representations = {}
        self.parserMPD()
        self.uri_re = re.compile(r'.+-(v\d+)n\d+\.m4s')

        self.pipeline.set_state(Gst.State.PAUSED)

    def parserMPD(self):
        req = urllib.request.urlopen(self.url)
        if req:
            tree = ET.parse(req)
            root = tree.getroot()

            adaptationSet = root[1][0]
            for rep in adaptationSet:
                if 'Representation' in rep.tag:
                    self.representations[rep.attrib['id']] = { 'width': rep.attrib['width'],
                                                    'height': rep.attrib['height'],
                                                    'fps': rep.attrib['frameRate'],
                                                    'bps': rep.attrib['bandwidth'] }
        else:
            print('Failed to read', self.url, flush=True)

    def metodoPlay(self):
        self.pipeline.set_state(Gst.State.PLAYING)

    def metodoPause(self):
        self.pipeline.set_state(Gst.State.PAUSED)

    def metodoStop(self):
        self.pipeline.set_state(Gst.State.NULL)

    def duracion(self):
        res, d = self.pipeline.query_duration(Gst.Format.TIME)
        if res:
            return d/1.0e9
        else:
            return 0

    def posicion(self):
        res, d = self.pipeline.query_position(Gst.Format.TIME)
        if res:
            return d/1.0e9
        else:
            return 0

    def on_sync_message(self, bus, message):
        if not message.get_structure():
            return True
        message_name = message.get_structure().get_name()

        if message_name == 'prepare-window-handle':
            imagesink = message.src
            imagesink.set_window_handle(self.windowId)

        if message.src.get_name().startswith('souphttpsrc'):
            info = message.get_structure()
            if info.get_name() == 'http-headers':
                for i in range(0, info.n_fields()):
                    n = info.nth_field_name(i)
                    if n == 'uri':
                        r = self.uri_re.fullmatch(info.get_value(n).strip())
                        if r:
                            rep_key = r.group(1)
                            if rep_key in self.representations:
                                self.current_representation = rep_key

        if message.src.get_name().startswith('dashdemux'):
            info = message.get_structure()
            if info.get_name() == 'adaptive-streaming-statistics':
                fragment_size = 0
                fragment_download_time = 0
                rep_key = ''
                for i in range(0,info.n_fields()):
                    n = info.nth_field_name(i)
                    if n == 'fragment-size':
                        fragment_size = info.get_value(n)
                    elif n == 'fragment-download-time':
                        fragment_download_time = info.get_value(n)
                    elif n == 'uri':
                        r = self.uri_re.fullmatch(info.get_value(n).strip())
                        if r:
                            rep_key = r.group(1)

                if fragment_download_time != 0 and rep_key.startswith('v'):
                    self.current_bandwidth = (float(fragment_size) / (float(fragment_download_time) / 1.0e9)) * 8 / 1.0e3

        return True

    def on_dash_pad_added(self, dashdemux, pad):
        template = pad.get_pad_template()
        name = template.name_template
        if name.startswith('video'):
            dashdemux.link(self.cola_video)
        elif name.startswith('audio'):
            dashdemux.link(self.cola_audio)

    def on_qt_pad_added(self, qtdemux, pad, parse):
        qtdemux.link(parse)

    def on_error(self, msg):
        print('on_error():', msg.parse_error())
        self.salir()

    def salir(self):
        self.pipeline.set_state(Gst.State.NULL)

    def volumen(self,valor):
        self.volume.set_property('volume', valor/10)

    def cambiaPosicion(self,valor):
        _,d = self.pipeline.query_duration(Gst.Format.TIME)
        new = int((valor/100.0) * d)
        self.pipeline.seek_simple(Gst.Format.TIME, Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT, new)
        self.pipeline.get_state(Gst.CLOCK_TIME_NONE)


class reproductor(QMainWindow):
    def __init__(self, url, ajustes):
        QMainWindow.__init__(self)
        self.ui = Ui_VentanaReproductor()
        self.ui.setupUi(self)

        self.ajustes = ajustes
        if self.ajustes == 0:
            self.arrayAjustes = 0
        else:
            self.arrayAjustes = [self.ajustes.anchura, self.ajustes.altura,
                                 self.ajustes.framerate, self.ajustes.bitrate,
                                 self.ajustes.info]

        windowId = self.ui.frameVideo.winId()
        self.estado = 'Paused'
        self.stream = stream(windowId, url, self.arrayAjustes)

        self.ui.botonPlay.clicked.connect(self.toogle)
        self.ui.botonStop.clicked.connect(self.stop)
        self.ui.botonGraficas.clicked.connect(self.abrirGraficas)

        self.ui.barraProgreso.reset()
        self.ui.barraAvanzar.setValue(0)
        self.actualizarBarra = threading.Thread(target=self.actualizarBarra,daemon=True)
        self.actualizarBarra.start()

        self.ui.barraVolumen.valueChanged.connect(self.volumen)

        self.actualizar_posicion = True
        self.ui.barraAvanzar.sliderPressed.connect(self.posicion_bloqueado)
        self.ui.barraAvanzar.sliderReleased.connect(self.posicion_desbloqueado)

        self.graficas = None

        self.show()

    def volumen(self,valor):
        self.stream.volumen(valor)

    def posicion_bloqueado(self):
        self.actualizar_posicion = False

    def posicion_desbloqueado(self):
        self.stream.cambiaPosicion(self.ui.barraAvanzar.value())
        self.actualizar_posicion = True
        p = int(self.stream.posicion())

        if self.graficas:
            self.graficas.actualizarEjeX(p)

    def actualizarBarra(self):
        while (True):
            if self.estado == 'Playing':
                d = self.stream.duracion()
                p = self.stream.posicion()
                if d != 0:
                    x = int(100*p/d)
                    if self.actualizar_posicion:
                        self.ui.barraAvanzar.setValue(x)
                        if self.graficas and self.stream.current_representation:
                            y = float(self.stream.current_representation[1:])
                            x = p
                            self.graficas.plot_current_data(x,y)
            time.sleep(0.3)


    def toogle(self):
        if self.estado == 'Paused':
            self.stream.metodoPlay()
            self.ui.botonPlay.setText('Pause')
            self.estado = 'Playing'
        else:
            self.stream.metodoPause()
            self.ui.botonPlay.setText('Play')
            self.estado = 'Paused'

    def stop(self):
        self.ui.barraAvanzar.setValue(0)
        self.ui.botonPlay.setText("Play")
        self.estado='Paused'
        self.stream.metodoStop()

    def abrirGraficas(self):
        self.graficas = graficas(self.stream.representations,self.stream.posicion())

    def closeEvent(self, event):
        self.stream.metodoStop()
        event.accept()
