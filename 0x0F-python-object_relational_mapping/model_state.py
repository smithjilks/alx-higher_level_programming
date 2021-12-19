#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ This class defines an object represtation of the table states
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
