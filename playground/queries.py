import sqlite3
import pandas as pd
from my_playground import *


def preview_data_in_db(table, conn):
    """(pd.read_sql) read table contents in a database connection istance to print first 10 rows

    Args:
        table (string): name of the table
        conn (db): connection to sqlite database instance 
    """
    sql = f"SELECT * FROM '{table}' limit 10;"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)
    
# def show_full_columns(table, conn):
#     sql = f"SHOW FULL COLUMNS FROM '{table}';"
#     dataframe = pd.read_sql(sql=sql, con=conn)
#     pprint(dataframe)
    
if __name__ == "__main__" :
    source_file = "../data/sample_data.csv"
    table_name = "sample_table"
    conn = sqlite3.connect("my_local.db")
    load_file_into_db(source_file, table_name, conn)
    preview_data_in_db(table_name, conn)
    # show_full_columns(table_name, conn)
    