import sqlite3
import pandas as pd
from my_playground import load_file_into_db


if __name__ == "__main__" :
    source_file = "../data/sample_data.csv"
    table_name = "sample_table"
    conn = sqlite3.connect("my_local.db")
    load_file_into_db(source_file, table_name, conn)
    