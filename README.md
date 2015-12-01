# Psiturk SQL to CSV!
  - helper to pull from a psiturk-formatted db and spit your back trialdata, eventdata, and questiondata.
  - idea is to be a replacement for download_datafiles in the psiturk CLI

## FEATURES:
  - **robust**: shouldn't crash not matter how exotic your data format (but let me know if does)
  - works with mySQL or sqlite.
  - can choose db\_name and table\_name of where data is, so **does not need to run inside a psiturk project folder**
  - can **choose path** and name of files saved
  - **tags each row** of trialdata, questiondata, and eventdata csv files with **subject id information**, which should make analysis easier.

## QUICKSTART:
```python
import psiturk_sql2csv

# sql database location
DB_URL = 'sqlite:///participants.db'  

# table name of the data in the db
TABLE_NAME = 'turkdemo'  # table name of data in the db

# sql2csv makes 3 files: [CSV_HEADER]_trialdata.csv, [CSV_HEADER]_eventdata.csv, and [CSV_HEADER]_questiondata.csv
CSV_HEADER = '/path/to/results/myResult'  

psiturk_sql2csv.sql2csv(DB_URL, TABLE_NAME, CSV_HEADER)
```

##### psiturk_sql2csv.py is modded off the retreiving data programatically script found [here in the psiturk docs](http://psiturk.readthedocs.org/en/latest/retrieving.html)
