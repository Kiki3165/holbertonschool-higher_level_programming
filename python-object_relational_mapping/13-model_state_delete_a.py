#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.ilike("%a%"))

    for state in query.all():
        session.delete(state)

    session.commit()