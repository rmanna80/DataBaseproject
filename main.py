# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:49:58 2022

@author: YourNameHere
"""

import csv
import pymysql
import configparser

# Get credentials to connect to database
config = configparser.ConfigParser()
config.read_file(open('credentials.txt'))  # point to the correct place where this file is!
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

# Choose schema
dbschema = 'rmanna'  # fill in whatever schema you are using (not table, SCHEMA)

# 1. Open database connection
dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

filename = 'player_stats_mattfeld.csv'
myRows = []  # set up an empty list to hold the data
try:
    with open(filename, 'r', encoding='utf-8') as myCSV:
        data = csv.reader(myCSV)
        next(myCSV)  # add this line to skip the first row
        for row in data:
            myRows.append(row)
    myCSV.close()
except FileNotFoundError:
    print('no file!')
print(myRows[0])
insertQuery = 'INSERT INTO player_stats () \
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
count = 0
for item in myRows:  # now process the list
    print(len(item))
    cursor.execute(insertQuery, (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10],\
                                 item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], \
                                 item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30],\
                                 item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40]))
