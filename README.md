# simple_analytics_pipeline

##### A simple example of loading data from CSV into SQLite DB, and then representing some data as charts.
  
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/org-not-included/simple_analytics_pipeline/main)](https://www.codefactor.io/repository/github/org-not-included/simple_analytics_pipeline)
[![GitHub languages](https://img.shields.io/github/languages/top/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/)
[![GitHub license](https://img.shields.io/github/license/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/blob/main/LICENSE)  
[![GitHub pull requests](https://img.shields.io/github/issues-pr/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/pulls)
[![GitHub issues](https://img.shields.io/github/issues/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/graphs/contributors)  
[![GitHub Release Date](https://img.shields.io/github/release-date/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/commits/main)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/graphs/commit-activity)  
[![GitHub forks](https://img.shields.io/github/forks/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/network)
[![GitHub stars](https://img.shields.io/github/stars/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/org-not-included/simple_analytics_pipeline)](https://github.com/org-not-included/simple_analytics_pipeline/watchers)
[![Twitter Follow](https://img.shields.io/twitter/follow/OrgNotIncluded?style=flat)](https://twitter.com/intent/follow?screen_name=OrgNotIncluded)  
---  
## Quick-Start
### Download Github Repo
```text
git clone https://github.com/org-not-included/simple_analytics_pipeline
cd simple_analytics_pipeline
```
### Load data and build sample chart
```text
source setup.sh
```
## ETL (Extract, Transform, Load) Terminology used within this code base
### An overview of what a Data Engieer does:
```
A data engineer is responsible for extracting (read), transforming (parse), and loading (save) the data in your database through a connection. They need to know:

1) Coding (Python, SQL)
2) Frameworks (Sqlite, Pandas)
```

### Read a csv file (data)
*Pre req: Use python3 sqlite to initialize a local db connection*

Use pandas (io) to convert the csv into a python object (dictionary). The reason to convert it into a dict is because you can then use pandas to initialize a database with a name of your choice that expects the data to be in the above format.
```
csv -> Pandas (io read) -> python dict -> Pandas (io write) -> sqlite table with table name
```
### Functions used within the code base:
*Pre req: Have a connection to your database*
```
import sqlite3
conn = sqlite3.connect(‘your_database_name’)
```
 
 Read a csv file and use pandas to read/convert it:
 Create a dataframe which is a pandas object (python dict with extra functionality) of the data that is read from csv.
```
 dataframe = pandas.read_csv(filename)
```

 Use Dataframe to write into your connection. Result is a table with the name of your choice stored in `your_database_name` specified by the connection:
```
dataframe.to_sql(‘your_table_name’, conn)
```