import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = None
sales = None

def cargarArchivo():
    global titanic,sales
    
    sales = pd.read_csv('C:/data/use_sales_data.csv')
    #titanic = pd.read_csv('C:/data/titanic.csv')

    #titanic = pd.read_csv('C:/data/titanic.csv')
    #titanic = pd.read_excel('C:/data/titanic.xlsx', sheet_name='Titanic_train')
    #print(titanic[['Name']])
    #print(titanic)

    #print(sales)

def cargarInfoGeneral():
    global titanic,sales

    print(sales.info())
    #print(titanic.corr())

# select Name,Age from titanic
def mostrarNombreEdad():
    global titanic,sales

    print(sales['Country'])

cargarArchivo()

cargarInfoGeneral()

mostrarNombreEdad()
