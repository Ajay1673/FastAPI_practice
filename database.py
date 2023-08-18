from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:ajayKrishna03@localhost/ajay')
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()