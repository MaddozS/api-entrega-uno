from pydantic import BaseModel

class ProfesorBase(BaseModel):
  nombres: str
  apellidos: str
  horasClase: int
  numeroEmpleado: int

class ProfesorCreate(ProfesorBase):
  pass

class Profesor(ProfesorBase):
  id: int
  class Config:
    orm_mode = True