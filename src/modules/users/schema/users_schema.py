from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    last_name: str
    email: str
    password: str
    phone: str
    identification: str