from sqlite3 import Error
import csv

from base.connection import create_connection
from base.factura import Factura

def select_table(connection1, sql_select_cliente):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(sql_select_cliente)

        # Datos de Base de Datos propiamente dicho
        facturas0 = cursor1.fetchall()        
        #print(facturas0)

        # Ejemplo de Clase Objetos con Base Datos
        facturas = list()
        factura1 = Factura(0,'',0,0.0,0.0)

        for factura0 in facturas0:
            factura1 = Factura(factura0[0],factura0[1],factura0[2],factura0[3],factura0[4])
            facturas.append(factura1)

        return facturas

    except Error as error1:
        print(error1)

    finally:
        if connection1:
            connection1.close()

def get_sql_select_factura():
    sql_select_factura_table =  """ 
                                    SELECT * FROM factura
                                """
    return sql_select_factura_table

def export_to_csv(facturas):
    # Crear un archivo CSV con los datos de DB

    with open('facturas.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Id', 'Producto', 'Cantidad','Precio','Total'])

        factura1:Factura = None

        for factura1 in facturas:
            writer.writerow([factura1.id,factura1.producto,factura1.cantidad,factura1.precio,factura1.total])



if __name__ == '__main__':
    # Paso 1 (Crear Conexion a BD)
    connection1 = create_connection("facturacion.db")
    #print("Conexion Realizada")
    # Facturas
    
    # Paso 2 (Crear SQL a ejecutar)
    sql_select_factura = get_sql_select_factura()
    #print(sql_select_factura)

    # Paso 3 (Ejecutar SQL y cargar en Clase/Lista Factura)
    facturas = select_table(connection1,sql_select_factura)
    #print(facturas)

    # Paso 4 Imprimir lista con clase/objetos
    print('----- Lista de Facturas ---')
    factura1:Factura = None

    for factura1 in facturas:
        factura1.cambiarValores()
        print(factura1.id,factura1.producto,factura1.cantidad,factura1.precio,factura1.total)

    # Paso 5 exportar datos de Lista/Clase/Objetos a Archivo CSV
    export_to_csv(facturas)