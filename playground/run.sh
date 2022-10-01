#!/bin/bash
echo "Enter dataframe to play around with dataframe.."
echo "or"
echo "Enter sqlite to play around with sqlite.."

read varname

if [[ "${varname}" == "dataframe" ]];then
  echo "Executing pandas dataframe methods to loop over data in dataframe"
  python3 playground.py dataframe
elif [[ "${varname}" == "sqlite" ]]; then 
  echo "Creating a sqlite database instance to load/read data from the database instance"
  python3 playground.py sqlite
else
  echo "Invalid input"
fi
