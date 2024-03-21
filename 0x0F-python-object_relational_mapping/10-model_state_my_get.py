#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Bind engine to Base
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for the State object with the given name
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()

if __name__ == "__main__":
    main()
