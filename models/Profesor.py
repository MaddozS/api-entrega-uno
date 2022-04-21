from pydantic import BaseModel


class Profesor(BaseModel):
    id: int
    nombres: str
    apellidos: str
    horasClase: int
    numeroEmpleado: int
