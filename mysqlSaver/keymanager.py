

class KeyManager:
    def __init__(self, connection):
        self.connection = connection



    def add_primary_key(self, table_name, primary_key_columns):
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW KEYS FROM `{table_name}` WHERE Key_name = 'PRIMARY'")
        if cursor.fetchone():
            print(f"Primary key already exists in table `{table_name}`. First remove it if needed.")
        else:
            query = f"ALTER TABLE `{table_name}` ADD PRIMARY KEY ({', '.join([f'`{col}`' for col in primary_key_columns])})"
            cursor.execute(query)
            self.connection.commit()
            print("Primary key added.")




    def drop_primary_key(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW KEYS FROM `{table_name}` WHERE Key_name = 'PRIMARY'")
        if cursor.fetchone():
            query = f"ALTER TABLE `{table_name}` DROP PRIMARY KEY"
            cursor.execute(query)
            self.connection.commit()
            print("Primary key dropped.")
        else:
            print("No primary key to drop.")



    def add_unique_key(self, table_name, unique_columns, constraint_name=None):
        cursor = self.connection.cursor()
        if not constraint_name:
            constraint_name = f"unique_{'_'.join(unique_columns)}"

        cursor.execute(f"SHOW INDEX FROM `{table_name}` WHERE Key_name = '{constraint_name}'")
        if cursor.fetchone():
            print(f"Unique key `{constraint_name}` already exists on `{table_name}`. Skipping creation.")
        else:
            query = f"ALTER TABLE `{table_name}` ADD CONSTRAINT `{constraint_name}` UNIQUE ({', '.join([f'`{col}`' for col in unique_columns])})"
            cursor.execute(query)
            self.connection.commit()
            print(f"Unique constraint `{constraint_name}` added on columns {unique_columns}.")




    def drop_unique_key(self, table_name, constraint_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SHOW INDEX FROM `{table_name}` WHERE Key_name = '{constraint_name}'")
        if cursor.fetchone():
            query = f"ALTER TABLE `{table_name}` DROP INDEX `{constraint_name}`"
            cursor.execute(query)
            self.connection.commit()
            print(f"Unique constraint `{constraint_name}` dropped.")
        else:
            print(f"No unique constraint named `{constraint_name}` found on `{table_name}`.")


