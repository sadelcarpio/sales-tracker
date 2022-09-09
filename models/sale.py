from sqlalchemy import Column, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from database import Base


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    id_store = Column(Integer, ForeignKey('store.id'))
    id_salesman = Column(Integer, ForeignKey('salesman.id'))
    id_product = Column(Integer, ForeignKey('product.id'))
    date = Column(Date)
    quantity = Column(Integer)
    registered_lat = Column(Float)
    registered_long = Column(Float)

    salesman = relationship('Salesman', back_populates='sales')
    store = relationship('Store', back_populates='sales')
    product = relationship('Product', back_populates='sales')
