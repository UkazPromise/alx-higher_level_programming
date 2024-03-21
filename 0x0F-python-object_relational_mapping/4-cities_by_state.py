#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cur = db.cursor()

    # Execute the SQL query to retrieve cities with their corresponding states
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
