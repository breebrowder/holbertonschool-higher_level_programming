#!/usr/bin/python3
""" Lists all cities of the state from the database hbtn_0e_4_usa """

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
        "SELECT cities.name FROM cities LEFT JOIN states ON cities.state_id\
        = states.id WHERE states.name = %s ORDER BY states.id ASC",
        (sys.argv[4],))

    columns = cur.fetchall()
    newcol = []
    print(', '.join('{}'.format(column[0]) for column in columns))

    # close all cursors
    cur.close()

    # close all databases
    db.close()
