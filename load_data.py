import sqlite3
import pandas as pd
from pprint import pprint

def load_file_to_db(filename, table, conn):
    # Read local csv file into pandas dataframe (dictionary object)
    dataframe = pd.read_csv(filename)
    # Load pandas dataframe into database (create a table called "sample_table")
    rows_affected = dataframe.to_sql(table, con=conn, if_exists="replace")
    return rows_affected


def preview_data(table, conn):
    sql = f"SELECT * FROM '{table}' limit 10;"
    dataframe = pd.read_sql_query(sql, con=conn)
    pprint(dataframe)


# Hard code table name and local file path
table_name = "sample_table"
source_file = "data/sample_data.csv"
# Initialize connection to database
conn = sqlite3.connect("my_local.db")
# Load the data into a table
rows_updated = load_file_to_db(filename=source_file, table=table_name, conn=conn)
# Preview the table
preview_data(table=table_name, conn=conn)