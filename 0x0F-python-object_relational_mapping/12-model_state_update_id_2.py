#!/usr/bin/python3
""" Change the name of a State object from the database hbtn_0e_6_usa """


from sys import argv
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    tmp = 'mysql+mysqldb://{}:{}@localhost/{}'\
          .format(argv[1], argv[2], argv[3])
    engine = create_engine(tmp)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.id == 2):
        instance.name = "New Mexico"
    session.commit()
    session.close()
