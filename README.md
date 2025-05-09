<h1 align="center"><strong>MySqlSaver</strong></h1>
<p align="center">
    Effortlessly save your pandas DataFrames into MySQL — with automatic table creation and support for primary keys and partitioning.
    <br><br>
    <a href="https://github.com/kasrakhaksar/mysqlsaver" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Repo-blue?logo=github" alt="GitHub" />
    </a>
</p>


A lightweight Python utility for saving pandas DataFrames to MySQL with automatic table creation and schema inference.

---

## 📥 Installation

```bash
pip install mysqlsaver
```

---

## 🔌 Connection

Create a connection to your MySQL database:

```python
from mysqlSaver.mysqlSaver import Connection

conn = Connection.connect(
    host="your_host",
    port="your_port",
    username="your_username",
    password="your_password",
    database="your_database"
)
```

---

## 📊 Data Operations

### Save a DataFrame

```python
from mysqlSaver.mysqlSaver import Saver
import pandas as pd

df = pd.DataFrame({...})
saver = Saver(conn)
saver.sql_saver(df, "table_name")
```

This function:
- Creates the table if it does not exist
- Inserts the DataFrame data

### Save with Primary Key

```python
saver.sql_saver_with_primarykey(df, "table_name", primary_key_list=["id"])
```

### Save with Primary Key and Auto-Update

```python
saver.sql_saver_with_primarykey_and_update(df, "table_name", primary_key_list=["id"])
```

This performs UPSERT using the primary key.

### Save with Unique Key (No Duplicate Insertions)

```python
saver.sql_saver_with_unique_key(df, "table_name")
```

### Update Table Based on Primary Key

```python
saver.sql_updater_with_primarykey(df, "table_name", primary_key_list=["id"])
```

---

## 🔍 Checker and Reader

```python
from mysqlSaver.mysqlSaver import CheckerAndReceiver

checker = CheckerAndReceiver(conn)
exists = checker.table_exist("table_name")
df = checker.read_table("table_name")
```

---

## 🛠️ Table and Database Creation

```python
from mysqlSaver.mysqlSaver import Creator

creator = Creator(conn)
creator.database_creator("new_database")
creator.create_table(df, "new_table")
```

---

## 🧩 Partitioning Tables

```python
from mysqlSaver.mysqlSaver import Partition

partitioner = Partition(conn)
partitioner.create_partition_table(
    df,
    "partitioned_table",
    range_key="your_date_column",
    primary_key_list=["id"],
    start_year_partition=2020,
    end_year_partition=2025
)
```


## 📎 Links

- 🔗 [GitHub Repository](https://github.com/kasrakhaksar/mysqlsaver)

---