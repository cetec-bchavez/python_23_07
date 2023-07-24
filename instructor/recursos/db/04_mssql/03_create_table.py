import pymssql
from base.connection import create_connection

def create_table(connection1, create_table_sql):
    
    try:
        cursor1 = connection1.cursor()
        
        cursor1.execute(create_table_sql)

    except:
        print('Error al Crear Tabla:')

    finally:
        if connection1:
            connection1.close()


def get_sql_create_table_factura():

    sql_create_factura_table = """ 
                                    CREATE TABLE dbo.factura (
                                        id INT PRIMARY KEY IDENTITY (1, 1),
                                        producto VARCHAR(250) NOT NULL,
                                        cantidad INT,
                                        precio DECIMAL(10,2),
                                        total DECIMAL(10,2)
                                    );
                                """
    return sql_create_factura_table


if __name__ == '__main__':
    # Conexion
    connection1 = create_connection('')

    # Tabla Factura 2
    sql_create_table_factura = get_sql_create_table_factura()
    create_table(connection1,sql_create_table_factura)
    print('Tabla Factura creada correctamente...')