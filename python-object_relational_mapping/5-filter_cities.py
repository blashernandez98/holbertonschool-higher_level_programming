#!/usr/bin/python3
""" Task 4 module """


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
        SELECT c.name, s.name
        FROM cities as c
        JOIN states as s
        ON c.state_id=s.id
        ORDER BY c.id
        """)
    rows = cur.fetchall()
    out = ""
    for row in rows:
        if row[1] == state:
            if out != "":
                out += ", "
            out += (row[0])
    print(out)
