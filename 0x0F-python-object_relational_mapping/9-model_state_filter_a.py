#!/usr/binI/python3
"""Prints the first State object containing the letter 'a' from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).first()

    if first_state_with_a:
        print("{}: {}".format(first_state_with_a.id, first_state_with_a.name))
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    main()
