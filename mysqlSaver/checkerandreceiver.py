import pandas as pd


class CheckerAndReceiver:
    def __init__(self , connection):
        self.connection = connection


    def read_table(self , table_name):
        sql_query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(sql_query, self.connection)
        return df
    


    def table_exist(self , table_name):
        
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        exist = cursor.fetchone()
        if exist == None:
            return False
        else:
            return True
        

    def database_exist(self , database_name):
        
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        exist = cursor.fetchone()
        if exist == None:
            return False
        else:
            return True

