import sqlite3
import pandas as pd
from my_playground import *

def load_file_into_db(filename, table, conn):
    """(dataframe.to_sql) load a table into a database connection istance

    Args:
        filename (string): name of the file
        table (string): name of the table
        conn (db): connection to sqlite database instance 
    """
    dataframe = pd.read_csv(filename)
    dataframe.to_sql(name=table, con=conn, if_exists="replace")

def preview_data_in_db(table, conn):
    """(pd.read_sql) read table contents in a database connection istance to print first 10 rows

    Args:
        table (string): name of the table
        conn (db): connection to sqlite database instance 
    """
    sql = f"SELECT * FROM '{table}' limit 10;"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)
    
def show_full_columns(table, conn):
    """show columns datatypes (schema)

    Args:
        table (string): table name
        conn (db): connection to sqlite database instance 
    """
    sql = f"SELECT * FROM PRAGMA_TABLE_INFO('{table}');"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)

def sql_where(table, conn):
    print("First names of employees with salary greater than 5000")
    sql = f"SELECT [first name] FROM '{table}' WHERE salary>5000;"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)
    print("First names, salary, gender of female employees with salary greater than 5000")
    sql = f"SELECT [first name], salary, gender FROM '{table}' WHERE salary>5000 AND gender='Female' AND [first name] IS NOT Null;"
    # sql2 = f"SELECT DISTINCT gender FROM {table} ORDER BY gender DESC;"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)

if __name__ == "__main__" :
    source_file = "../data/employees.csv"
    table = "employees"
    conn = sqlite3.connect("employees.db")
    load_file_into_db(source_file, table, conn)
    preview_data_in_db(table, conn)
    show_full_columns(table, conn)
    sql_where(table, conn)
    