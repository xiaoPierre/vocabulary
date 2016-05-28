from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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
