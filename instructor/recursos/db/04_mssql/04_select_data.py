import pymssql
# import mysql.connector as database

from base.connection import create_connection
from base.factura import Factura

def select_table(connection1, sql_select_factura):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(sql_select_factura)

        facturas0 = cursor1.fetchall()

        facturas = list()
        factura1 = Factura(0,'',0,0.0,0.0)

        for factura0 in facturas0:
            factura1 = Factura(factura0[0],factura0[1],factura0[2],factura0[3],factura0[4])
            facturas.append(factura1)

        return facturas

    except:
        print('Error')

    finally:
        if connection1:
            connection1.close()

def get_sql_select_factura():
    sql_select_factura_table =  """ 
                                    SELECT * FROM factura
                                """
    return sql_select_factura_table


if __name__ == '__main__':
    connection1 = create_connection("")
    
    # Facturas
    sql_select_factura = get_sql_select_factura()
    facturas = select_table(connection1,sql_select_factura)
    
    print('----- Lista de Facturas ---')
    factura1:Factura = None

    for factura1 in facturas:
        print(factura1.id,factura1.producto,factura1.cantidad,factura1.precio,factura1.total)