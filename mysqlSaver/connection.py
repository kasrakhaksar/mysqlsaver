import pymysql



class Connection:
    def __init__(self) -> None:
        pass


    def connect(host , port , username , password , database):
        try:
            return pymysql.connect(host=host, port=int(port), user=username , password=password , database=database)
        except :
            print('This connection does not exist')