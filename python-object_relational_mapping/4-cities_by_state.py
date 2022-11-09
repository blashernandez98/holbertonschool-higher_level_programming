#!/usr/bin/python3
""" Task 4 module """


import MySQLdb
import sys

args = sys.argv
if len(args) == 4:
    user = args[1]
    passwd = args[2]
    datab = args[3]
    db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute("""
        SELECT c.id, c.name, s.name
        FROM cities as c\
        JOIN states AS s
        ON s.id=c.state_id
        ORDER BY c.id
        """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
