import pandas as pd
from pprint import pprint
import sys
import sqlite3

def read_data(filename):
    """(pd.read_csv) uses pandas to read a csv file and convert it to a dataframe

    Args:
        filename (string): a csv filename 
    """
    dataframe = pd.read_csv(filename)
    print('Printing dataframe...')
    print(dataframe)
    return dataframe
    
def df_iter_rows(df):
    """(dataframe.iterrows) uses dataframe.iterrows to print first 3 rows in df

    Args:
        df (dataframe): pandas dataframe
    """
    print('(ITER_ROWS) Printing first 3 rows in the dataframe...')
    for index, row in df.iterrows():
        if index == 3: break
        print('ROW:', index)
        print(row)
    
def df_iter_tuples(df):
    """(dataframe.itertuples) uses dataframe.itertuples to print first 3 row tuples in df

    Args:
        df (dataframe): pandas dataframe
    """
    index = 0
    print('(ITER_TUPLES) Printing first 3 tuples in the dataframe...')
    for tuple in df.itertuples():
        if index == 3: break
        print('TUPLE:', index)
        print(tuple)
        index = index + 1 

def df_iter_columns(df):
    """converts df into a python list to print first 3 columns in df

    Args:
        df (dataframe): pandas dataframe
    """
    columns = list(df)
    index = 0
    print('(COLUMNS) Printing first 3 columns...')
    for i in columns:
        if index == 3: break
        print('COLUMN:', index)
        print (df[i])
        index = index + 1

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

if __name__ == "__main__":
    source_file = "../data/sample_data.csv"
    table_name = "sample_table"
    conn = sqlite3.connect("my_playground.db")
    if (sys.argv[1] == 'df-read'):
        df = read_data(filename=source_file)
    elif (sys.argv[1] == 'df-iterrows'):
        df = read_data(filename=source_file)
        df_iter_rows(df)
    elif (sys.argv[1] == 'df-itertuples'):
        df = read_data(filename=source_file)
        df_iter_tuples(df)
    elif (sys.argv[1] == 'df-itercolumns'):
        df = read_data(filename=source_file)
        df_iter_columns(df)
    elif (sys.argv[1] == 'db-load'):
        load_file_into_db(source_file, table_name, conn)
    elif (sys.argv[1] == 'db-load-read'):
        load_file_into_db(source_file, table_name, conn)
        preview_data_in_db(table_name, conn)