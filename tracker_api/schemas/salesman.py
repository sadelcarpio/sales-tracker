from pydantic import BaseModel


class SalesmanBase(BaseModel):
    name: str
    dni: int


class Salesman(SalesmanBase):
    id: int

    class Config:
        orm_mode = True
