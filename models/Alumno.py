from pydantic import BaseModel

class Alumno(BaseModel):
    id: int
    nombres: str
    apellidos: str
    matricula: str
    promedio: float
