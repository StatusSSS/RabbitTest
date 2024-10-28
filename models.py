from sqlmodel import SQLModel



class User(SQLModel):
    name: str
    email: str
    password: str

