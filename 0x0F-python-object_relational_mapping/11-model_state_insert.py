#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
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

    # Create new State object with the given name
    new_state_name = sys.argv[4]
    new_state = State(name=new_state_name)

    # Add the new State object to the session
    session.add(new_state)
    session.commit()

    # Query the database for the new State object and print its ID
    new_instance = session.query(State).filter_by(name=new_state_name).first()
    if new_instance:
        print(new_instance.id)
    else:
        print("State not found")

    # Close session
    session.close()
