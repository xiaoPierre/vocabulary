from sqlalchemy import Column, String, create_engine, Integer, Date, ForeignKey, Float, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'userTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(40))
    lastName = Column(String(40))
    email = Column(String(60))
    password = Column(String(40))
    level = Column(Integer())
    ranking = Column(Integer())

class WordLearning(Base):
    __tablename__ = 'userWordTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    mastery = Column(Integer())
    user_id = Column(Integer, ForeignKey('userTable.id'))
    user = relationship('User')

class Record(Base):
    __tablename__ = 'userRecordTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date())
    point =Column(Integer())
    time = Column(Integer())
    questionAnswered = Column(Integer())
    wordMastered = Column(Integer())
    user_id = Column(Integer, ForeignKey('userTable.id'))
    user = relationship('User')

class Preference(Base):
    __tablename__ = 'userPreferenceTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String())

    user_id = Column(Integer, ForeignKey('userTable.id'))
    user = relationship('User')

engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
Base.metadata.create_all(engine)