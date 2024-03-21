#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa where the name contains the provided argument (using wildcards)."""

import MySQLdb
import sys


def main():
    """Lists states containing the provided name (with wildcards) from hbtn_0e_0_usa."""

    if len(sys.argv) != 5:
        print("Usage: ./script_name <username> <password> <database> <search_term>")
        return

    username, password, db_name, search_term = sys.argv[1:]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Create the SQL query with parameterized input and wildcards
        sql = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

        # Execute the query with the search term with wildcards
        cur.execute(sql, (f"%{search_term}%",))

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
