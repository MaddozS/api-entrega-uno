from typing import Union
from pydantic import BaseModel

class AlumnoBase(BaseModel):
  nombres: str
  apellidos: str
  matricula: str
  promedio: float
  fotoPerfilUrl: Union[str, None] = None

class AlumnoCreate(AlumnoBase):
  pass

class Alumno(AlumnoBase):
  id: int
  class Config:
    orm_mode = True