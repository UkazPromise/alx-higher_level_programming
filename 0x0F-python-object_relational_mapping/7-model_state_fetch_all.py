#!/usr/bin/python3I

"""Creates all tables defined by model classes in 'model_state.py' within the database."""

from model_state import Base, State
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Create all tables based on model definitions in model_state.py."""

    username, password, db_name = sys.argv[1:]

    try:
        # Create a SQLAlchemy engine
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

        # Create all tables based on model classes
        Base.metadata.create_all(engine)

        # Create a sessionmaker object
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query all State objects (assuming State is defined in model_state.py)
        states = session.query(State).order_by(State.id)

        # Print state information (modify separator if needed)
        for state in states:
            print(state.id, state.name, sep=", ")

    except exc.SQLAlchemyError as err:
        print(f"Error creating tables: {err}")

    finally:
        # Close the session to release resources
        if session:
            session.close()
