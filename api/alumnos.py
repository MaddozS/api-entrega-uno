
import os
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from typing import List

from sqlalchemy.orm import Session
from aws.client import S3Client

from db_app.database import engine, Base, get_db
from db_app.schemas.Alumno import AlumnoCreate, Alumno
from db_app.crud import alumnos

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("", status_code=200, response_model=List[Alumno])
def get_alumnos(db: Session = Depends(get_db)):
  return alumnos.get_alumnos(db)

@router.post("", status_code=201, )
def post_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
  return alumnos.create_alumno(db, alumno)

@router.get("/{id_alumno}", status_code=200)
def get_alumno(id_alumno: int, db: Session = Depends(get_db)):

  alumno_db = alumnos.get_alumno(db, id_alumno)

  if not alumno_db:
    raise HTTPException(status_code=404, detail="Alumno no encontrado")
  
  return alumno_db

@router.put("/{id_alumno}", status_code=200)
def put_alumno(id_alumno: int, alumno: AlumnoCreate, db: Session = Depends(get_db)):
  
  alumno_db = alumnos.get_alumno(db, id_alumno)

  if not alumno_db:
    raise HTTPException(status_code=404, detail="Alumno no encontrado")
  
  return alumnos.edit_alumno(db, id_alumno, alumno)

@router.delete("/{id_alumno}")
def delete_alumno(id_alumno: int, db: Session = Depends(get_db)):
    
    alumno_db = alumnos.get_alumno(db, id_alumno)
  
    if not alumno_db:
      raise HTTPException(status_code=404, detail="Alumno no encontrado")
    
    return alumnos.delete_alumno(db, id_alumno)

@router.post("/{id_alumno}/fotoPerfil")
def add_foto_perfil_alumno(id_alumno: int, foto: UploadFile = File(...), db: Session = Depends(get_db)):
    alumno_db = alumnos.get_alumno(db, id_alumno)

    if not alumno_db:
      raise HTTPException(status_code=404, detail="Alumno no encontrado")

    split_file_name = os.path.splitext(foto.filename)  #split the file name into two different path (string + extention)
    file_name_unique = alumno_db.matricula
    file_extension = split_file_name[1]
    
    data = foto.file._file
    s3 = S3Client()
    url = s3.upload_file(data, f"alumnos/{file_name_unique}{file_extension}")

    alumno_foto = AlumnoCreate(
      nombres = alumno_db.nombres,
      apellidos = alumno_db.apellidos,
      matricula = alumno_db.matricula,
      promedio=alumno_db.promedio,
      fotoPerfilUrl=url)

    return alumnos.edit_alumno(db, id_alumno, alumno_foto)