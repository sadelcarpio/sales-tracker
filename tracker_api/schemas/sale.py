import datetime

from pydantic import BaseModel


class SaleBase(BaseModel):
    date: datetime.date
    quantity: int
    registered_lat: float
    registered_long: float


class SaleCreate(SaleBase):
    pass


class Sale(SaleBase):
    id: int
    id_salesman: int
    id_store: int
    id_product: int

    class Config:
        orm_mode = True
