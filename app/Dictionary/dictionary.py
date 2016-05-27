from app.Model.Word import *
import pickle

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


def suggestWord(prefix):
    with open('dawgFile.dawg', 'rb') as dawgFile:
        dawgObj = pickle.load(dawgFile)
        words = dawgObj.keys(prefix)
        if len(words) > 6:
            return words[0:6]
        else:
            return dawgObj.keys(prefix)

