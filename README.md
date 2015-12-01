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
```
# example_psiturk_sql2csv.py
import psiturk_sql2csv

DB_URL = 'sqlite:///participants.db'  # works with mySQL and sqlite
TABLE_NAME = 'turkdemo'  # table name of data in the db
# what you want to call the output.
# sql2csv makes 3 files: [CSV_HEADER]_trialdata.csv, [CSV_HEADER]_eventdata.csv, and [CSV_HEADER]_questiondata.csv
# remember that this name can include a path to whereever you want to save, eg:
#   CSV_HEADER = '/home/coolman666/results/omgJBYouDaBes' will save to the folder /home/coolman666/results/
CSV_HEADER = 'example'  
# **note that this version also tags every row of all three csvs with id information about the subject.
# **feel free to change the idFields list in psiturk_sql2csv.py too add/drop idFields
psiturk_sql2csv.sql2csv(DB_URL, TABLE_NAME, CSV_HEADER)
```
##### psiturk_sql2csv.py is modded off the retreiving data programatically script found [here in the psiturk docs](http://psiturk.readthedocs.org/en/latest/retrieving.html)
