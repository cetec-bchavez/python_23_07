import os

import general.General as gn
import sales.sales_pd as sl

opcion=0

def mostrarMenu():
    global opcion

    print('1.- Mostrar Ejemplo Fechas')
    print('2.- Mostrar Sales Grafico')
    print('0.- Salir')

    opcion=int(input('Ingrese una Opcion:'))



while True:

    input('Teclee Enter...')
    os.system('cls')

    mostrarMenu()

    if(opcion==0):
        break
    elif(opcion==1):
        gn.exec_load_data_fechas()
    elif(opcion==2):
        sl.salesCargarArchivo()
        sl.salesMostrarFilasCosto3Grafico()
