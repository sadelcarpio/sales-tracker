from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Salesman(Base):
    __tablename__ = 'salesman'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dni = Column(String(8), nullable=False)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String(60), nullable=False)

    sales = relationship('Sale', back_populates='salesman')
