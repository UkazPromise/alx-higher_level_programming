#!/usr/bin/python3

"""Prints the first State object that contains the letter 'a' from the database hbtn_0e_6_usa."""

from model_state import Base, State
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Prints the first State object containing the letter 'a' (limited to one result)."""

    username, password, db_name = sys.argv[1:]

    try:
        # Create a SQLAlchemy engine
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

        # Create a sessionmaker object
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Filter State objects containing 'a' (limited to one) and fetch the first
        first_state = session.query(State).filter(State.name.like('%a%')).first()

        if first_state:  # Check if a matching state was found
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("No state found")

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")

    finally:
        # Close the session
        if session:
            session.close()
