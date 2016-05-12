from sqlalchemy import Column, String, create_engine, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import requests
from lxml import etree
from time import sleep
import re, os

Base = declarative_base()

class User(Base):
    __tablename__ = 'userTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(40))
    lastName = Column(String(40))
    email = Column(String(60))
    password = Column(String(40))
    level = Column(Integer())

class Word(Base):
    __tablename__ = 'wordTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ortho = Column(String(40))
    phono = Column(String(40))
    lemme = Column(String(40))
    cgram = Column(String(10))
    genre = Column(String())
    infover = Column(String())
    freqlemfilms = Column(Float())
    freqlemlivres = Column(Float())
    freqfilms = Column(Float())
    freqlivres = Column(Float())

    def __str__(self):
        return "I am " + self.ortho + " and my frequence is " + str(self.freqlemfilms)




engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
Base.metadata.create_all(engine)