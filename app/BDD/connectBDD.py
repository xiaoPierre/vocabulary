from contextlib import contextmanager
from app.Model.Word import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.misc.etendu import etendu

@contextmanager
def connectBDD():
    """ Creates a context with an open SQLAlchemy session.
    """
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test", convert_unicode=True)
    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    yield db_session
    db_session.close()
    connection.close()


if __name__ == '__main__':



    with connectBDD() as session:
        length = len(etendu)

        for i in range(0,length -1):
            upper = etendu[i]
            lower = etendu[i+1]
            words = session.query(Word).filter(Word.freqlemfilms>=lower)\
                .filter(Word.freqlemfilms<=upper)
            lemmes = set()
            for word in words:
                lemmes.add(word.lemme)
            print("mots entre " + str(lower) + " et " + str(upper) + " sont " + str(len(lemmes)))
        print(length)