import sys,gi

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

from PySide2.QtWidgets import QMainWindow
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtCore import Qt
from ui_ventanagraficas import Ui_VentanaGraficas

from images import *


class graficas(QMainWindow):
    def __init__(self, representations, posicionActual):
        QMainWindow.__init__(self)
        self.ui = Ui_VentanaGraficas()
        self.ui.setupUi(self)
        self.representations = representations
        self.posicionActual = int(posicionActual)

        self.chartView = QtCharts.QChartView(parent=self.ui.widget)
        self.chartView.setMinimumSize(self.ui.widget.width(), self.ui.widget.height());
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart = QtCharts.QChart()
        self.chartView.setChart(self.chart)
        self.chart.setTitle('Adaptación')

        self.model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(self.model)

        for i in self.representations:
            diccionarioRepresentacion = self.representations.get(i)
            textoRepresentacion=i
            textoRepresentacion+='-->'
            for k in diccionarioRepresentacion.keys():
                textoRepresentacion+=' '
                textoRepresentacion+=k
                textoRepresentacion+=' '
                if k=='bps':
                    valorMbps = str(round((float(diccionarioRepresentacion.get(k))/1.0e6),3))
                    textoRepresentacion+=valorMbps
                else:
                    textoRepresentacion+=diccionarioRepresentacion.get(k)

            item = QtGui.QStandardItem(textoRepresentacion)
            self.model.appendRow(item)

        self.prepare_chart()
        self.show()


    def prepare_chart(self):
        self.axisX = QtCharts.QValueAxis()
        self.axisX.setRange(self.posicionActual, self.posicionActual+9);
        self.axisX.setTickCount(10)
        self.axisX.setTitleText('Tiempo (s)')
        self.chart.addAxis(self.axisX, Qt.AlignBottom)

        axisY = QtCharts.QCategoryAxis()
        max = 0
        min = sys.maxsize

        counter = 0
        for k in self.representations:
            value = int(k[1:])
            if max < value:
                max = value
            if min > value:
                min = value
            axisY.append(k,value)
            counter += 1
        axisY.setMax(max)
        axisY.setMin(min)
        axisY.setStartValue(min)
        axisY.setTitleText('Nivel')
        axisY.setLabelsPosition(QtCharts.QCategoryAxis.AxisLabelsPositionOnValue)
        self.chart.addAxis(axisY, Qt.AlignLeft)

        axisY2 = QtCharts.QCategoryAxis()
        axisY2.setLabelsPosition(QtCharts.QCategoryAxis.AxisLabelsPositionOnValue)
        axisY2.setTitleText('Bandwidth (Mbps)')
        self.current_bandwidth = 0.0
        for k in self.representations:
            value = int(k[1:])
            # ¡No puede haber dos label iguales! Hacen falta 3 decimales para distinguirlos.
            label = '%.3f' % (float(self.representations[k]['bps'])/1.0e6)
            axisY2.append(label,value)
        self.chart.addAxis(axisY2, Qt.AlignRight)
        axisY2.setMax(max)
        axisY2.setMin(min)
        axisY2.setStartValue(min)

        # Serie de datos para gráfica del nivel de representación
        self.series = QtCharts.QLineSeries()
        self.series.setName('Nivel de representación')
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(axisY)

    def plot_current_data(self, x, y):
        if self.axisX.max() < x:
            self.axisX.setMax(self.axisX.max()+10)
        self.series.append(x,y)

    def actualizarEjeX(self, p):
        self.series.clear()
        self.axisX.setRange(p, p+9)

    def closeEvent(self, event):
        self.series.clear()
        event.accept()
