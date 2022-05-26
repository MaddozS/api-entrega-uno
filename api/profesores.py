from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from db_app.database import engine, Base, get_db
from db_app.schemas.Profesor import ProfesorCreate, Profesor
from db_app.crud import profesores

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("", status_code=200, response_model=List[Profesor])
def get_profesores(db: Session = Depends(get_db)):
  return profesores.get_profesores(db)

@router.post("", status_code=201 )
def post_alumno(alumno: ProfesorCreate, db: Session = Depends(get_db)):
  return profesores.create_profesor(db, alumno)

@router.get("/{id_profesor}", status_code=200)
def get_profesor(id_profesor: int, db: Session = Depends(get_db)):

  profesor_db = profesores.get_profesor(db, id_profesor)

  if not profesor_db:
    raise HTTPException(status_code=404, detail="Profesor no encontrado")
  
  return profesor_db

@router.put("/{id_profesor}", status_code=200)
def put_profesor(id_profesor: int, profesor: ProfesorCreate, db: Session = Depends(get_db)):
  
  profesor_db = profesores.get_profesor(db, id_profesor)

  if not profesor_db:
    raise HTTPException(status_code=404, detail="Profesor no encontrado")
  
  return profesores.edit_profesor(db, id_profesor, profesor)

@router.delete("/{id_profesor}")
def delete_profesor(id_profesor: int, db: Session = Depends(get_db)):
    
    profesor_db = profesores.get_profesor(db, id_profesor)
  
    if not profesor_db:
      raise HTTPException(status_code=404, detail="Alumno no encontrado")
    
    return profesores.delete_profesor(db, id_profesor)