import MySQLdb
import sys

args = sys.argv
if len(args) == 4:
    user = args[1]
    passwd = args[2]
    datab = args[3]

    db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=datab)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
