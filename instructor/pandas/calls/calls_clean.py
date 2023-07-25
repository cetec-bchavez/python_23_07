import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

calls:pd.DataFrame = None

def load_data():
    global calls

    calls = pd.read_excel('C:/data/Customer_Call_List.xlsx')

def show_info():
    global calls

    print(calls.info())

def eliminar_columna():
    global calls

    calls = calls.drop(columns=['Not_Useful_Column','Do_Not_Contact','Paying Customer'])

def crear_columna():
    global calls

    calls['Name_All'] = calls['First_Name'] + calls['Last_Name']

    print(calls['Name_All'])

load_data()

show_info()

crear_columna()
#eliminar_columna()

show_info()