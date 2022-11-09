#!/usr/bin/python3
""" Task 3 module """


import MySQLdb
import sys

args = sys.argv
if len(args) == 5:
    user = args[1]
    passwd = args[2]
    datab = args[3]
    state = args[4]
    db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute("""
        SELECT * FROM states\
        WHERE name = %(search)s\
        ORDER BY id
        """, {'search': state})
    rows = cur.fetchall()
    for row in rows:
        if row[1] == state:
            print(row)
