import pandas as pd

def read_data(filename):
    """uses pandas to read a csv file and convert it to a dataframe

    Args:
        filename (string): a csv filename 
    """
    dataframe = pd.read_csv(filename)
    print('Printing dataframe...')
    print(dataframe)
    return dataframe
    
def df_iter_rows(df):
    """uses dataframe.iterrows to print first 3 rows in df

    Args:
        df (dataframe): pandas dataframe
    """
    print('(ITER_ROWS) Printing first 3 rows in the dataframe...')
    for index, row in df.iterrows():
        if index == 3 :
            break
        print('ROW:', index)
        print(row)
    
def df_iter_tuples(df):
    """uses dataframe.itertuples to print first 3 row tuples in df

    Args:
        df (dataframe): pandas dataframe
    """
    index = 0
    print('(ITER_TUPLES) Printing first 3 tuples in the dataframe...')
    for tuple in df.itertuples():
        if index == 3 :
            break
        print('TUPLE:', index)
        print(tuple)
        index = index + 1    

if __name__ == "__main__":
    source_file = "../data/sample_data.csv"
    df = read_data(filename=source_file)
    df_iter_rows(df)
    df_iter_tuples(df)