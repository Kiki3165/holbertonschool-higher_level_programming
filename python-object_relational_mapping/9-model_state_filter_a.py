#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f'mysql://{db_user}:{db_password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in query:
        print(f"{state.id}: {state.name}")

    session.close()