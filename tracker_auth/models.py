from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'salesman'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dni = Column(Integer, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String(60), nullable=False)
