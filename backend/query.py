#!/usr/bin/env python
import pprint
import sqlite3

def query(queryText):
  # Location of database file
  database_file = "database.db"

  # Open SQLite database connection
  conn = sqlite3.connect(database_file)
  cur = conn.cursor()

  # Sample query
  result = cur.execute(queryText)
  pprint.pprint(cur.fetchall())
