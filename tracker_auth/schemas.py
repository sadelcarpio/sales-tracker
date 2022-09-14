from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    dni: int
    username: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    dni: int
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
