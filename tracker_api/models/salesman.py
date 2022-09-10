from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Salesman(Base):
    __tablename__ = 'salesman'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dni = Column(Integer, nullable=False)

    sales = relationship('Sale', back_populates='salesman')
