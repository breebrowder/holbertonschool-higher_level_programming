#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    columns = cur.fetchall()
    for column in columns:
        print(state)

    # close all cursors
    cur.close()

    # close all databases
    db.close()
