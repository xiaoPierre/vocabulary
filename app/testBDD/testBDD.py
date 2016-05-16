import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.Word import *
from app.model.User import *


engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


query = session.query(Word).order_by(Word.freqfilms).filter(Word.freqfilms>10).filter(Word.freqfilms<15)
for word in query:

    print(word)

query = session.query(User).all()
for user in query:
    session.delete(user)

session.close()