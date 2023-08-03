import typing
from PyQt5.QtWidgets import QWidget
from grafico.base.TableModel import TableModel

import pandas as pd

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt

class Pantalla1(QtWidgets.QMainWindow):

    def __init__(self, data):
        super().__init__()

        self.data=data
        self.model=TableModel(data)

        self.table = QtWidgets.QTableView()

        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

