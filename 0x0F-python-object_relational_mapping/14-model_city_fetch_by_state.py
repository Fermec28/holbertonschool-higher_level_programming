#!/usr/bin/python3
""" lists all State objects from the database"""


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name).join(City)
    results = results.order_by(City.id).all()
    for row in results:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
