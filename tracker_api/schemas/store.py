from pydantic import BaseModel


class StoreBase(BaseModel):
    ruc_or_dni: str
    name: str
    lat: float
    long: float


class StoreCreate(StoreBase):
    pass


class Store(StoreBase):
    id: int

    class Config:
        orm_mode = True
