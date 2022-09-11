#!/usr/bin/python3
"""Safe from MySQL injections"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name=%s
         ORDER BY id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
