from operator import truediv

from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id: int
    Titulo: str
    Descripcion: str
    Disponible: bool = True
    Precio: float
    Tipo: str