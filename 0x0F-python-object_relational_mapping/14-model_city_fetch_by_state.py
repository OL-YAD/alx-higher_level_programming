#!/usr/bin/python3
"""Print all City objs from db 'hbtn_0e_14_usa'"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(i.State.name, i.City.id, i.City.name))
