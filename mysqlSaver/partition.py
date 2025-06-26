from .checkerandreceiver import CheckerAndReceiver


class Partition:
    def __init__(self  , connection ):
        self.connection = connection



    def create_partition_table(self , df , table_name , range_key , primary_key_list , start_year_partition , end_year_partition):

        
        if not CheckerAndReceiver(self.connection).table_exist(table_name):
            start_year = start_year_partition
            start_month = 1
            end_year = end_year_partition
            end_month = 12
            year = start_year
            month = start_month
            partition_query = ''
            first_iteration = True

            while year <= end_year:
                while (year < end_year and month <= 12) or (year == end_year and month <= end_month):
                    partition_name = f"p{year}m{month:02}"
                    partition_value = int(f"{year}{month:02}32")
                    partition_clause = f"PARTITION `{partition_name}` VALUES LESS THAN ({partition_value}) ENGINE = InnoDB"
                    
                    if first_iteration:
                        partition_query += partition_clause
                        first_iteration = False
                    else:
                        partition_query += f", {partition_clause}"
                    
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                        
                break

            cursor = self.connection.cursor()
            column_data_types = {"int32":'INT' , 'int64': 'INT', 'float64': 'FLOAT', 'datetime64': 'DATETIME', 'bool': 'BOOL', 'object': 'VARCHAR(70)'}
            columns = ', '.join([f'`{column}` {column_data_types[str(data_type)]}' for column, data_type in df.dtypes.items()])
            query_set_partition = f'''CREATE TABLE {table_name} ({columns}, KEY `{table_name}_index` ({' , '.join(primary_key_list)})) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci PARTITION BY RANGE (`{range_key}`) ({partition_query})'''
            cursor.execute(query_set_partition)
            self.connection.commit()
        else:
            pass