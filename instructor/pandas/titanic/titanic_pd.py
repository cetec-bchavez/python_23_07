import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = None

def cargarArchivo():
    global titanic

    titanic = pd.read_csv('C:/data/titanic.csv')
    #titanic = pd.read_excel('C:/data/titanic.xlsx', sheet_name='Titanic_train')

    print(titanic)

cargarArchivo()