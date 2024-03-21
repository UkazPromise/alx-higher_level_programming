#!/usr/bin/python3
"""Script to link class to table in database"""

import sys
from sqlalchemy import create_engine
from model_state import Base

def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Create engine
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create tables
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
