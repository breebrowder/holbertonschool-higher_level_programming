#!/usr/bin/python3
""" write a script that takes in arguments and displays all values """

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
    cur.execute(
        "SELECT * from states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],))

    columns = cur.fetchall()
    for column in columns:
            print("{}".format(column))

    # close all cursors
    cur.close()

    # close all databases
    db.close()
