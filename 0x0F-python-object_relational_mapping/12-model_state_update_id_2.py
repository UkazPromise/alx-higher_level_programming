#!/usr/bin/python3
"""Updates the name of the State object with the given ID"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_id".format(sys.argv[0]))
        sys.exit(1)

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Bind engine to Base
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the State object with the given ID
    state_id = int(sys.argv[4])
    state = session.query(State).filter_by(id=state_id).first()

    if state:
        # Update the name of the State object
        state.name = 'New Mexico'
        session.commit()
        print(state.id)
    else:
        print("State not found")

    # Close session
    session.close()
