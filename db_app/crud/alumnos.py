from sqlalchemy.orm import Session

from db_app.models.Alumno import Alumno 
from db_app.schemas.Alumno import AlumnoCreate

def get_alumno(db: Session, alumno_id: int):
  return db.query(Alumno).filter(Alumno.id == alumno_id).first()

def get_alumnos(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Alumno).offset(skip).limit(limit).all()

def create_alumno(db: Session, alumno: AlumnoCreate):
    alumno_db = Alumno(
      nombres=alumno.nombres,
      apellidos=alumno.apellidos,
      matricula=alumno.matricula,
      promedio=alumno.promedio,
      fotoPerfilUrl=alumno.fotoPerfilUrl
    )

    db.add(alumno_db)
    db.commit()
    db.refresh(alumno_db)
    return alumno_db

def edit_alumno(db: Session, alumno_id: int, alumno: AlumnoCreate):
  put_alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

  put_alumno.nombres = alumno.nombres
  put_alumno.apellidos = alumno.apellidos
  put_alumno.matricula = alumno.matricula
  put_alumno.promedio = alumno.promedio
  put_alumno.fotoPerfilUrl = alumno.fotoPerfilUrl

  db.commit()
  db.refresh(put_alumno)

  return put_alumno

def delete_alumno(db: Session, alumno_id: int):
  alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

  db.delete(alumno)
  db.commit()

  return alumno