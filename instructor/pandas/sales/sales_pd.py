import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic:pd.DataFrame = None
sales:pd.DataFrame = None

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
    print(sales.shape)
    #print(titanic.corr())

# select Country from sales
# TOP, LIMIT/OFFSET --> head
def mostrarPais():
    global titanic,sales
    
    print(sales['Country'].head(5))

# select Country,State from sales
# LIMIT / OFFSET
def mostrarPaisEstado():
    global titanic,sales
    
    cs = sales[['Country','State']].tail(5)

    print(cs.shape)

#select DISTINCT Country from sales
def mostrarPaisesUnico():
    global titanic,sales
    
    print(sales['Country'].unique())

cargarArchivo()

#cargarInfoGeneral()
#mostrarPais()
#mostrarPaisEstado()

mostrarPaisesUnico()