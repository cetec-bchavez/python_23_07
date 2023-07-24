import pandas as pd
import numpy as np
import matplotlib as mp

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = None

def cargarArchivo():
    global titanic

    #titanic = pd.read_csv('C:/data/titanic.csv')
    #titanic = pd.read_excel('C:/data/titanic.xlsx', sheet_name='Titanic_train')
    base=pd.read_excel(r'C:/Users/julia/OneDrive/Documentos/GitHub/python_23_07/data/titanic.xlsx',  sheet_name='Titanic_train')

    print(base)

cargarArchivo()


