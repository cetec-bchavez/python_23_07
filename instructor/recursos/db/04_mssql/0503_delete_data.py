import pymssql
#import mysql.connector as database

from base.connection import create_connection
from base.factura import Factura

def delete_table(connection1, sql_delete_table,factura1):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(sql_delete_table,factura1)

        connection1.commit()
        
        return cursor1.lastrowid

    except:
        print('Error al Eliminar Cliente:')

    finally:
        if connection1:
            connection1.close()

def get_sql_delete_table_factura():
    sql_delete_factura_table =  ''' DELETE FROM factura
                                                WHERE id = %s
                                '''

    return sql_delete_factura_table


def get_factura(factura0:Factura):
     factura1 = (factura0.id,)
     #factura1 = (2,)

     return factura1


if __name__ == '__main__':

    # Factura
    connection1 = create_connection("")

    sql_delete_table_factura = get_sql_delete_table_factura()
    factura0 = Factura(29,'',0,0,0)
    factura1 = get_factura(factura0)
    delete_table(connection1,sql_delete_table_factura,factura1)
    print('Factura eliminado correctamente...')
    