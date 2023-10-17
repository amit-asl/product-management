from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
engine = create_engine('postgresql://amit:12345@pg:5432/aslpm')

conn = engine.connect()

Base = declarative_base()

local_session = sessionmaker(engine)
session = Session(bind=engine)