import pymssql

# sudo pip install pymssql

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    
    try:                
        conn = pymssql.connect(
                    server='yourserver.database.windows.net', 
                    user='yourusername@yourserver', 
                    password='yourpassword', 
                    database='AdventureWorks')

        return conn
        
    except:
        print('Error')


#if __name__ == '__main__':
#    create_connection()