import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic:pd.DataFrame = None
sales:pd.DataFrame = None

def salesCargarArchivo():
    global titanic,sales
    
    sales = pd.read_csv('C:/data/use_sales_data.csv')
    #titanic = pd.read_csv('C:/data/titanic.csv')

    #titanic = pd.read_csv('C:/data/titanic.csv')
    #titanic = pd.read_excel('C:/data/titanic.xlsx', sheet_name='Titanic_train')
    #print(titanic[['Name']])
    #print(titanic)

    #print(sales)

def salesCargarInfoGeneral():
    global titanic,sales

    print(sales.info())
    print(sales.shape)
    #print(titanic.corr())

# select Country from sales
# TOP, LIMIT/OFFSET --> head
def salesMostrarPais():
    global titanic,sales
    
    print(sales['Country'].head(5))

# select Country,State from sales
# LIMIT / OFFSET
def salesMostrarPaisEstado():
    global titanic,sales
    
    cs = sales[['Country','State']].tail(5)

    print(cs.shape)

def salesMostrarPaisEstadoReturn():
    global titanic,sales
    
    cs = sales[['Country','State']].tail(5)

    return cs

#select DISTINCT Country from sales
def salesMostrarPaisesUnico():
    global sales
    
    print(sales['Country'].unique())

def salesMostrarFilasCosto():
    global sales
    
    filas1 =sales.loc[sales['Unit_Cost']>200]

    print(filas1)

def salesMostrarFilasCostoReturn():
    global sales
    
    filas1 =sales.loc[sales['Unit_Cost']>200]

    return filas1

    #filas1.to_csv('Costos_mayor_50.csv')

def salesMostrarFilasCosto2():
    global sales
    
    filas1 =sales[sales['Unit_Cost']>1900]

    print(filas1)

def salesMostrarFilasCosto3():
    global sales
    
    filas1 =sales[(sales['Unit_Cost']>1900) & (sales['Month']=='May')]

    print(filas1)

def salesMostrarFilasCosto3Grafico():
    global sales
    
    filas1 =sales[(sales['Unit_Cost']>1900) & (sales['Month']=='May')]

    filas1.plot(kind='hist')
    #filas1['Unit_Cost'].plot(kind='hist')
    #filas1.plot(kind='scatter',x='Country',y='Unit_Cost')
    plt.show()

    #print(filas1)

#salesCargarArchivo()

#salesMostrarFilasCosto3Grafico()
#salesMostrarFilasCosto3()
#salesMostrarFilasCosto2()
#salesMostrarFilasCosto()
#salesCargarInfoGeneral()
#salesMostrarPais()
#salesMostrarPaisEstado()
#salesMostrarPaisesUnico()