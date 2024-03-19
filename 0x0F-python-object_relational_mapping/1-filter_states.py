#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa, starting with 'N' (uppercase), sorted by ID."""

import MySQLdb
import sys


def main():
    """Lists states starting with 'N' from hbtn_0e_0_usa."""

    if len(sys.argv) != 4:
        print("Usage: ./script_name <username> <password> <database>")
        return

    username, password, db_name = sys.argv[1:]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Execute the query to filter states by name starting with 'N' and order by id
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

        # Fetch all results
        rows = cur.fetchall()

        for row in rows:
            print(row)  # Print each state tuple

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
