from .creator import Creator
from tqdm import tqdm
from .checkerandreceiver import CheckerAndReceiver



class Saver:
    def __init__(self ,  connection):
        self.connection = connection


    def sql_saver(self , df , table_name):

        if not CheckerAndReceiver(self.connection).table_exist(table_name):
            Creator(self.connection).create_table(df , table_name)

        cursor = self.connection.cursor()
        columns = ', '.join([f'`{column}`' for column in df.columns])
        values_str = ','.join(['%s'] * len(df.columns))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str})"
        for row in tqdm(df.values):
            data = tuple(row)
            cursor.execute(query, data)
        self.connection.commit()




    def sql_saver_with_primarykey(self , df , table_name , primary_key_list):

        if not CheckerAndReceiver(self.connection).table_exist(table_name):
            Creator(self.connection).create_table(df , table_name)

        cursor = self.connection.cursor()
        columns = ', '.join([f'`{column}`' for column in df.columns])
        values_str = ','.join(['%s'] * len(df.columns))
        query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({values_str});"
        self.connection.commit()
        query3 = f"ALTER TABLE {table_name} DROP PRIMARY KEY;"
        query_check_key = f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY';"
        cursor.execute(query_check_key)
        if cursor.fetchone() is not None:
            cursor.execute(query3)
            self.connection.commit()
        else:
            pass
        query2 = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({' , '.join(primary_key_list)})"
        cursor.execute(query2)
        self.connection.commit()
        
        for row in tqdm(df.values):
            data = tuple(row)
            cursor.execute(query, data)
        self.connection.commit()





    def sql_saver_with_primarykey_and_update(self , df , table_name , primary_key_list):

        
        if not CheckerAndReceiver(self.connection).table_exist(table_name):
            Creator(self.connection).create_table(df , table_name)

        cursor = self.connection.cursor()
        columns = ', '.join([f'`{column}`' for column in df.columns])
        values_str = ','.join(['%s'] * len(df.columns))
        query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({values_str});"
        self.connection.commit()
        update_str = ', '.join([f'`{column}` = VALUES(`{column}`)' for column in df.columns])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str}) ON DUPLICATE KEY UPDATE {update_str};"
        self.connection.commit()
        query3 = f"ALTER TABLE {table_name} DROP PRIMARY KEY;"
        query_check_key = f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY';"
        cursor.execute(query_check_key)
        if cursor.fetchone() is not None:
            cursor.execute(query3)
            self.connection.commit()
        else:
            pass
        query2 = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({' , '.join(primary_key_list)})"
        cursor.execute(query2)
        self.connection.commit()
        
        for row in tqdm(df.values):
            data = tuple(row)
            cursor.execute(query, data)
        self.connection.commit()



    def sql_saver_with_unique_key(self , df , table_name):
        if not CheckerAndReceiver(self.connection).table_exist(table_name):
            Creator(self.connection).create_table(df , table_name)

        cursor = self.connection.cursor()
        columns = ', '.join([f'`{column}`' for column in df.columns])
        values_str = ', '.join(['%s'] * len(df.columns))

        query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({values_str});"

        for row in tqdm(df.values):
            data = tuple(row)
            cursor.execute(query, data)
        self.connection.commit()



    def sql_updater_with_primarykey(self , df , table_name , primary_key_list):
        cursor = self.connection.cursor()

        for row in tqdm(df.values):
            primary_key_values = tuple(row[df.columns.get_loc(pk)] for pk in primary_key_list)
            set_statements = ', '.join([f'`{column}` = %s' for column in df.columns if column not in primary_key_list])
            query = f"UPDATE {table_name} SET {set_statements} WHERE {' AND '.join([f'`{pk}` = %s' for pk in primary_key_list])};"
            data = tuple(row[df.columns.get_loc(column)] for column in df.columns if column not in primary_key_list) + primary_key_values
            cursor.execute(query, data)

        self.connection.commit()

