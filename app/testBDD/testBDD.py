
from app.Model.Word import *
from app.Model.User import *


engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


query = session.query(Word).order_by(Word.freqfilms).filter(Word.freqfilms>10).filter(Word.freqfilms<15)
for word in query:
    print(word)

query = session.query(User).all()
for user in query:
    session.delete(user)
query = session.query(Word)
with open('wordList.txt', 'w', encoding='utf-8') as wordListe:
    for word in query:
        wordListe.write(word.ortho)
        wordListe.write('\n')

session.close()