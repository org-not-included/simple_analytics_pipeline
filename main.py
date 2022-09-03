import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint
import sqlite3


def load_file_to_db(filename, table, conn):
    # Read local csv file into pandas dataframe (dictionary object)
    dataframe = pd.read_csv(filename)
    # Load pandas dataframe into database (create a table called "sample_table")
    dataframe.to_sql(name=table, con=conn, if_exists="replace")


def preview_data(table, conn):
    # Print 10 rows of data from table
    sql = f"SELECT * FROM '{table}' limit 10;"
    dataframe = pd.read_sql(sql=sql, con=conn)
    pprint(dataframe)
    # pprint(dataframe.columns)


def create_chart(sql, conn, x, y):
    # Fetch query results as pandas dataframe (dictionary object)
    dataframe = pd.read_sql_query(sql, con=conn)
    # pprint(dataframe)
    dataframe.plot(x=x, y=y, kind="bar")
    plt.show()



if __name__ == "__main__":
    # Hard code table name and local file path
    table_name = "sample_table"
    source_file = "data/sample_data.csv"
    # Initialize connection to database
    conn = sqlite3.connect("my_local.db")
    # Load the data into a table
    load_file_to_db(filename=source_file, table=table_name, conn=conn)
    # Preview the table
    preview_data(table=table_name, conn=conn)

    charts_sql = f"""
    Select
        AVG(Value) as avg_val,
        Variable_category
        from
            {table_name}
        GROUP BY Variable_category
        ORDER BY AVG(Value)
    """

    create_chart(sql=charts_sql, conn=conn, x="Variable_category", y="avg_val")
