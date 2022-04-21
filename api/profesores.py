
from fastapi import APIRouter, Response

from models.Profesor import Profesor

router = APIRouter()

index = 1 
profesores = {}

@router.get("", status_code=200)
def get_profesores():
  return profesores

@router.post("", status_code=201)
def post_profesor(profesor: Profesor):
  profesores[profesor.id] = profesor
  return profesor

@router.get("/{id_profesor}", status_code=200)
def get_profesor(id_profesor: int, response: Response):

  if id_profesor in profesores:
    profesor = profesores[id_profesor]
    return profesor
  else:
    response.status_code = 404
    return {'message': 'Profesor no encontrado'}

@router.put("/{id_profesor}", status_code=201)
def put_profesor(id_profesor: int, profesor: Profesor):
  profesores[id_profesor] = profesor
  return profesor

@router.delete("/{id_profesor}")
def delete_profesor(id_profesor: int, response: Response):
  if id_profesor in profesores:
    del profesores[id_profesor]
    return {'message': 'Profesor eliminado'}
  else:
    response.status_code = 404
    return {'message': 'Profesor no encontrado'}