import pymssql
#import mysql.connector as database

from base.connection import create_connection
from base.factura import Factura

def update_table(connection1, sql_update_table,cliente1):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(sql_update_table,cliente1)

        connection1.commit()
        
        return cursor1.lastrowid

    except:
        print('Error al Ingresar Nuevo Cliente:')

    finally:
        if connection1:
            connection1.close()


def get_sql_update_table_factura():
    sql_update_factura_table =  ''' UPDATE  factura
                                            SET producto = %s ,
                                                cantidad = %s ,
                                                precio = %s ,
                                                total = %s                                                
                                            WHERE id = %s
                                '''
                                

    return sql_update_factura_table


def get_factura(factura0:Factura):
     factura1 = (factura0.producto, factura0.cantidad, factura0.precio, factura0.total,factura0.id)

     #factura1 = ('Teclado', 6,8, 48)

     return factura1


if __name__ == '__main__':

    # Cliente
    connection1 = create_connection('')

    sql_update_table_factura = get_sql_update_table_factura()
    factura0 = Factura(30,'Teclado', 6,8,48)
    factura1 = get_factura(factura0)
    update_table(connection1,sql_update_table_factura,factura1)
    print('Factura actualizado correctamente...')