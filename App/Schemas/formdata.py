from pydantic import BaseModel

class FormData(BaseModel):
    name: str
    email: str
    phone: str
