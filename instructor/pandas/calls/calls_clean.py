import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

calls:pd.DataFrame = None

def callsLoad_data():
    global calls

    calls = pd.read_excel('C:/data/Customer_Call_List.xlsx')

def callsShow_info():
    global calls

    print(calls.info())

def callsEliminar_columna():
    global calls

    calls = calls.drop(columns=['Not_Useful_Column','Do_Not_Contact','Paying Customer'])

def callsCrear_columna():
    global calls

    calls['Name_All'] = calls['First_Name'] + calls['Last_Name']

    print(calls['Name_All'])

callsLoad_data()

callsShow_info()

callsCrear_columna()
#callsEliminar_columna()

callsShow_info()