import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:          
        # Codigo Principal      
        conn = sqlite3.connect(db_file)                
        # print(sqlite3.version)

        return conn
        
    except Error as e:
        print(e)