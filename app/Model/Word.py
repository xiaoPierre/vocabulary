from sqlalchemy import Column, String, create_engine, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect


Base = declarative_base()

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

    def getLength(self):
        return len(self.ortho)

    def isLemme(self):
        return self.ortho == self.lemme

    def __str__(self):
        str1 =  "I am " + self.ortho + " and my frequence is " + str(self.freqfilms)
        str2 = " my lemme is " + self.lemme
        str3 = " my categorie is " + self.cgram
        return str1+str2+str3




engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
Base.metadata.create_all(engine)