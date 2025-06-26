

class Creator:
    def __init__(self  , connection):
        self.connection =connection


    def create_table(self , df , table_name):
        cursor = self.connection.cursor()
        
        column_data_types = {"int32": 'INT', 'int64': 'INT', 'float64': 'FLOAT', 'datetime64': 'DATETIME', 'bool': 'BOOL', 'object': 'LONGTEXT'}
        columns = []

        for column, data_type in df.dtypes.items():
            if data_type == 'object':
                max_length = df[column].str.len().max()
                if max_length >= 70:
                    columns.append(f"`{column}` LONGTEXT")
                else:
                    columns.append(f"`{column}` VARCHAR(70)")
            else:
                columns.append(f"`{column}` {column_data_types[str(data_type)]}")

        columns_str = ', '.join(columns)
        
        query = f"CREATE TABLE {table_name} ({columns_str})"
        cursor.execute(query)
        self.connection.commit()


    def database_creator(self , database_name):
        
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        exist = cursor.fetchone()
        if not exist:
            cursor.execute(f"CREATE DATABASE {database_name}")
        else:
            print('Database is exist')
