#!/bin/bash
echo "Enter an option (number):"
echo "1. df-read"
echo "2. df-iterrows"
echo "3. df-itertuples"
echo "4. df-itercolumns"
echo "5. load-read-db"

read varname

if [[ "${varname}" == "1" ]];then
  echo "(pd.read_csv) uses pandas to read a csv file and convert it to a dataframe"
  python3 playground.py df-read
elif [[ "${varname}" == "2" ]]; then 
  echo "(dataframe.iterrows) uses dataframe.iterrows to print first 3 rows in df"
  python3 playground.py df-iterrows
elif [[ "${varname}" == "3" ]]; then 
  echo "(dataframe.itertuples) uses dataframe.itertuples to print first 3 row tuples in df"
  python3 playground.py df-itertuples
elif [[ "${varname}" == "4" ]]; then 
  python3 playground.py df-itercolumns
elif [[ "${varname}" == "5" ]]; then 
  echo "(dataframe.to_sql) load a table into a database connection istance"
  echo "(pd.read_sql) read table contents in a database connection istance to print first 10 rows"
  python3 playground.py db-load-read
else
  echo "Invalid input"
fi
