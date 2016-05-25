from app.Model.Word import *

def findLemme(word):
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Word).filter(Word.ortho==word)
    if query.count() == 0:
        session.close()
        return ''
    for item in query:
        if item.lemme == item.ortho:
            session.close()
            return item.lemme
    session.close()
    return query[0].lemme

findLemme('adfasf')

def suggestWord(word):
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Word).filter(Word.ortho == word)
    if query.count() != 0:
        return query[0].lemme
    else:
        return word