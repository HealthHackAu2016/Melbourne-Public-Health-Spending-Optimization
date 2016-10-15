#!/usr/bin/env python
import csv
import os
import sqlite3

def import_csv():

  # Location of database file
  database_file = "database.db"
  # Location of CSV(s) to import
  file_dir = "."

  # Create an SQLite database in the current directory
  conn = sqlite3.connect(database_file)
  cur = conn.cursor()
  # Create a table for our data
  cur.execute("""CREATE TABLE IF NOT EXISTS
  data(
    'fval'                                    REAL,
    'Prophylactic zinc supplementation'       REAL,
    'Vitamin A supplementation'               REAL,
    'Complementary feeding education'         REAL,
    'Public provision of complementary foods' REAL,
    'Breastfeeding promotion'                 REAL,
    'Balanced energy-protein supplementation' REAL,
    'Multiple micronutrient supplementation'  REAL
    )
  """)

  # Create list of all CSV files in the specified directory
  csvs = [ f for f in os.listdir(file_dir) if
      f.endswith('.csv') and
      os.path.isfile(os.path.join(file_dir, f)) ]
  # Iterate through CSVs and import each row into the database table
  # FIXME: This doesn't do deduplication of rows
  for f in csvs:
    print(f)
    with open(os.path.join(file_dir, f)) as f_handle:
      reader = csv.reader(f_handle)
      for field in reader:
        cur.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?);", field)

  # Delete header row
  cur.execute("DELETE FROM data WHERE fval='fval';")

  conn.commit()
  conn.close()

import_csv()
