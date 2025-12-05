from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connstring = "sqlite:///./test.db"
engine = create_engine(url=connstring)
sessionlocal = sessionmaker(autocommit=False,bind=engine,autoflush=False)
base = declarative_base()
base.metadata.create_all(engine)
def get_db():
    db = sessionlocal()
    try:
        yield db
        
    finally:
        db.close()