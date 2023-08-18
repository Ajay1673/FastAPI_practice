from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import base, engine

class User(base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False, unique=True)
    age = Column(String(10),nullable=False)
    gender = Column(String(50),nullable=False)
    dob = Column(String(50),nullable=False)

base.metadata.create_all(bind=engine)