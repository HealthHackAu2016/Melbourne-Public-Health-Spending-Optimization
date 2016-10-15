# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:04:49 2016

@author: ruth
"""

import sqlite3

def query(queryText):
  # Location of database file
  database_file = "database.db"
  # Open SQLite database connection
  conn = sqlite3.connect(database_file)
  cur = conn.cursor()
  # do the query
  result = cur.execute(queryText)
  return cur.fetchall()

def getResult(interventionConstraints):
    # interventionConstraints is a dictionary with this structure:
    # interventionConstraints = {}
    # interventionConstraints[intervention] = {}
    # example:
    # interventionConstraints[breastfeeding][min] = 10
    # interventionConstraints[breastfeeding][max] = 100

    # make the SQL query string
    queryString = 'SELECT * FROM data WHERE'
    for intervention in interventionConstraints:
        minStr = str(interventionConstraints[intervention]['min'])   
        maxStr = str(interventionConstraints[intervention]['max']) 
        stringToAdd = " " + '"' + intervention + '"' + " BETWEEN '" + minStr + "' AND '" + maxStr + "' AND"
        queryString += stringToAdd
   
   # remove the final 'AND' and put a semicolon on the end
    queryString = queryString[:len(queryString)-4]   
    queryString += ';'
   
   # SQL call to get all entries that meet the criteria
    results = query(queryString)
   
   # search through the set returned and return the best
    best = results[0]   
    for result in results:
        if result[0] < best[0]:
            best = result
   # returb the best         
    return best
    
    
interventionConstraints = {}
interventionConstraints["Breastfeeding promotion"] = {}
interventionConstraints["Breastfeeding promotion"]['min'] = 1000
interventionConstraints["Breastfeeding promotion"]['max'] = 2000
interventionConstraints["Multiple micronutrient supplementation"] = {}
interventionConstraints["Multiple micronutrient supplementation"]['min'] = 1000
interventionConstraints["Multiple micronutrient supplementation"]['max'] = 2000
    
best = getResult(interventionConstraints)
print best    