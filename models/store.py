from sqlalchemy import Column, Integer, String, BigInteger, Float
from sqlalchemy.orm import relationship

from database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    ruc_or_dni = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    lat = Column(Float)
    long = Column(Float)

    sales = relationship('Sale', back_populates='store')
