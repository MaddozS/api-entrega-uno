
from fastapi import APIRouter, Response

from models.Alumno import Alumno

router = APIRouter()

index = 1 
alumnos = {}

@router.get("", status_code=200)
def get_alumnos():
  return alumnos

@router.post("", status_code=201, )
def post_alumno(alumno: Alumno):
  alumnos[alumno.id] = alumno
  return alumno

@router.get("/{id_alumno}", status_code=200)
def get_alumno(id_alumno: int, response: Response):

  if id_alumno in alumnos:
    alumno = alumnos[id_alumno]
    return alumno
  else:
    response.status_code = 404
    return {'message': 'Alumno no encontrado'}

@router.put("/{id_alumno}", status_code=200)
def put_alumno(id_alumno: int, alumno: Alumno):
  alumnos[id_alumno] = alumno
  return alumno

@router.delete("/{id_alumno}")
def delete_alumno(id_alumno: int, response: Response):
  if id_alumno in alumnos:
    del alumnos[id_alumno]
    return {'message': 'Alumno eliminado'}
  else:
    response.status_code = 404
    return {'message': 'Alumno no encontrado'}
