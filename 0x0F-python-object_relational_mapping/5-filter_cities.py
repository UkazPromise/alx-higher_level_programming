#!/usr/bin/python3

"""Lists all cities from the database hbtn_0e_4_usa for a given state, using parameterized queries."""

import MySQLdb
import sys


def main():
    """Lists cities for the given state from hbtn_0e_4_usa, using execute() only once."""

    if len(sys.argv) != 5:
        print("Usage: ./script_name <username> <password> <database> <state_name>")
        return

    username, password, db_name, state_name = sys.argv[1:]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)

        # Create a cursor object
        cursor = db.cursor()

        # Create the SQL query with parameterized input and a subquery to fetch the state ID
        sql = """
            SELECT cities.name
            FROM cities
            WHERE cities.state_id = (
                SELECT states.id
                FROM states
                WHERE states.name = %s
            )
            ORDER BY cities.id ASC
        """

        # Execute the query with the state name
        cursor.execute(sql, (state_name,))

        # Fetch all results (city names)
        city_names = cursor.fetchall()

        # Print city names separated by commas
        print(", ".join([name for name in city_names]))  # Use list comprehension for efficiency

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
