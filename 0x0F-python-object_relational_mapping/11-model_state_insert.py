#!/usr/bin/python3
""" List all State objects that contain the letter a from the database """


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

    Siana = State(name='Louisiana')
    session.add(Siana)
    session.commit()
    print(Siana.id)

    session.close()
