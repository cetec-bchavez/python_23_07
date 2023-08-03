import sys

import pandas as pd
from grafico.Pantalla1 import Pantalla1
from grafico.Pantalla2 import Pantalla2
import sales.sales_pd as sl

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt

def showPantalla1():

    app = QtWidgets.QApplication(sys.argv)

    sl.salesCargarArchivo()

    data = sl.salesMostrarFilasCostoReturn()

    pantall1= Pantalla1(data)

    pantall1.show()

    app.exec_()

def showPantalla2():

    app = QtWidgets.QApplication(sys.argv)

    sl.salesCargarArchivo()

    data = sl.salesMostrarFilasCostoReturn()
    data2 = sl.salesMostrarPaisEstadoReturn()

    pantall1= Pantalla2(data,data2,data)

    pantall1.show()

    app.exec_()


#showPantalla1()

showPantalla2()
