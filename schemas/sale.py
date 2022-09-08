from pydantic import BaseModel
import datetime


class SaleBase(BaseModel):
    date: datetime.date
    quantity: int


class SaleCreate(SaleBase):
    pass


class Sale(SaleBase):
    id: int
    id_salesman: int
    id_store: int
    id_product: int

    class Config:
        orm_mode = True
