from grafico.base.TableModel import TableModel

import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Pantalla2(QtWidgets.QMainWindow):

    def __init__(self,data1,data2,data3):
        super().__init__()

        self.table = QtWidgets.QTableView()

        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        
        self.model = TableModel(self.data1)

        self.table.setModel(self.model)

        #self.setCentralWidget(self.table)

        self.createHorizontalLayout()

        self.verticalGroupBox = QGroupBox('')
        windowLayout = QVBoxLayout()
        
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.table)
        
        self.verticalGroupBox.setLayout(windowLayout)
        
        self.setCentralWidget(self.verticalGroupBox)
        #self.setCentralWidget(self.horizontalGroupBox)
        #self.setLayout(windowLayout)


    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox('')
        layout = QHBoxLayout()
        
        buttonBlue = QPushButton('Proceso 1', self)
        buttonBlue.clicked.connect(self.on_click1)
        layout.addWidget(buttonBlue)
        
        buttonRed = QPushButton('Proceso 2', self)
        buttonRed.clicked.connect(self.on_click2)
        layout.addWidget(buttonRed)
        
        buttonGreen = QPushButton('Proceso 3', self)
        buttonGreen.clicked.connect(self.on_click3)
        layout.addWidget(buttonGreen)
        
        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click1(self):
        self.model = TableModel(self.data1)
        self.table.setModel(self.model)
    
        #print('PyQt5 button click 1')

    @pyqtSlot()
    def on_click2(self):
        self.model = TableModel(self.data2)
        self.table.setModel(self.model)

        #print('PyQt5 button click 2')

    @pyqtSlot()
    def on_click3(self):
        self.model = TableModel(self.data3)
        self.table.setModel(self.model)

        #print('PyQt5 button click 3')