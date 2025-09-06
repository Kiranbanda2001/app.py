from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///cricbuzz.db"  # change to PostgreSQL/MySQL if needed

def get_engine():
    return create_engine(DB_URL, echo=False)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()