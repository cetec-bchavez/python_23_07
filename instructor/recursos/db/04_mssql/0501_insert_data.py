import pymssql
#import mysql.connector as database

from base.connection import create_connection
from base.factura import Factura

def insert_table(connection1, sql_insert_table_sql,factura1):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(sql_insert_table_sql,factura1)

        connection1.commit()

        print("Id=",cursor1.lastrowid)

        return cursor1.lastrowid

    except:
        print('Error al Ingresar Nuevo Cliente:')

    finally:
        if connection1:
            connection1.close()

def get_sql_insert_table_factura():
    sql_insert_factura_table = ''' 
                                INSERT factura(producto,cantidad,precio,total)
                                VALUES(%s,%s,%s,%s) 
                                '''
                                

    return sql_insert_factura_table


def get_factura(factura0:Factura):
     factura1 = (factura0.producto, factura0.cantidad, factura0.precio, factura0.total)

     #factura1 = ('Mouse', 5, 7.0, 35.0)
     return factura1

if __name__ == '__main__':

    # Factura
    
    connection1 = create_connection("")

    sql_insert_table_factura = get_sql_insert_table_factura()
    factura0 = Factura(1,'Mouse Pad',5,7,35)
    factura1 = get_factura(factura0)
    insert_table(connection1,sql_insert_table_factura,factura1)
    print('Nuevo Factura creado correctamente...')
    