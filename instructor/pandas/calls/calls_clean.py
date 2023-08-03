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

def callsReemplazarColumna():
    global calls

    calls['First_Name'] = calls['First_Name'].str.upper()
    #calls['First_Name'] = calls['First_Name'].str.replace('VERDADERO','V')

    print(calls['First_Name'])

def callsReemplazarColumnaFila():
    global calls
    #Regex --> Like
    for indice in calls.index:
        if calls.loc[indice,'Do_Not_Contact'] == 'Y' or calls.loc[indice,'Do_Not_Contact'] == 'YES':
            calls.loc[indice,'Do_Not_Contact'] = 'SI'

    print(calls['Do_Not_Contact'])


callsLoad_data()

callsReemplazarColumnaFila()

#callsReemplazarColumna()
#callsShow_info()
#callsCrear_columna()
#callsEliminar_columna()
#callsShow_info()