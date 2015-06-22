from todo import app

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(app.config["DATABASE"], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import todo.models
    Base.metadata.create_all(bind=engine)

def delete_all_entries():
    Base.metadata.drop_all(bind=engine)
