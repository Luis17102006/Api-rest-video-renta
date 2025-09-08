from pydantic import BaseModel, EmailStr
from typing import Optional

class Usuario(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: str