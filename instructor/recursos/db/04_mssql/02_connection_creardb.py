import pymssql


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection1 = None

    try:
        connection1 = pymssql.connect(
                    server='yourserver.database.windows.net', 
                    user='yourusername@yourserver', 
                    password='yourpassword', 
                    database='AdventureWorks')
        
        #print(sqlite3.version)

        return connection1
        
    except:
        print('Error de Conexion:')

    finally:
        if connection1:
            connection1.close()


# Descomentar para Crear DB
"""
if __name__ == '__main__':
    create_connection("facturacion.db")
    print('Base de Datos Facturacion Creada...')
"""