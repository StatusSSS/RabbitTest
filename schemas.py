from pydantic import BaseModel



class Account(BaseModel):
    login: str
    password: str
    email: str

