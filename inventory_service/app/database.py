from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./inventory.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()
