
<p style="text-align: center; font-size: 24px; font-weight: bold;">
    <b>MySqlSaver</b>
    <br>
    <a href="https://github.com/kasrakhaksar/mysqlsaver" target="_blank"><img src="https://img.shields.io/badge/GitHub-Repo-blue?logo=github" alt="GitHub" style="vertical-align: middle; margin-right: 10px;" /></a>
</p>



First of all , you must connect to your mysql database with this function :

```
from mysqlSaver.mysqlSaver import *

your_connection = Connection.connect("your_host" , "your_port" , "your_username" , "your_password" , "your_databasename")
```

When you make connection to your owen database , you can use "your_connection" variable to use other function like this , for example :

```
from mysqlSaver.mysqlSaver import *
import pandas as pd

your_connection = Connection.connect("your_host" , "your_port" , "your_username" , "your_password" , "your_databasename")

df = pd.DataFrame({"name" : ['john'] , "lastname" : ["doe"] , 'age' : [19]})
df_saver = Saver(your_connection)
df_saver.sql_saver(df , "your_table")
```


In this function, at first, according to the create_table function, the table is created based on the type of each column in the dataframe .
You can use other functions such as partition and primarykey and etc. in the same way.
But some functions like sql_saver_with_primarykey(), we need to give more inputs to be saved in the desired way. For example:


```
from mysqlSaver.mysqlSaver import *
import pandas as pd

your_connection = Connection.connect("your_host" , "your_port" , "your_username" , "your_password" , "your_databasename")

df = pd.DataFrame({"name" : ['john'] , "lastname" : ["doe"] , 'age' : [19]})
df_saver_by_primary_key = Saver(your_connection)
df_saver_by_primary_key.sql_saver_with_primarykey(df , "your_table" , ['lastname'])
```

In the code above, you give the function a primary key by typing list and it will set and save your table based on that primary key.