#!/usr/bin/python3
""" lists all State objects that contain the letter a """


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State.id).filter_by(name=argv[4]).first()
    if state:
        print(state[0])
    else:
        print("Not found")
    session.close()
