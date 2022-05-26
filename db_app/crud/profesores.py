from sqlalchemy.orm import Session

from db_app.models.Profesor import Profesor
from db_app.schemas.Profesor import ProfesorCreate

def get_profesor(db: Session, profesor_id: int):
  return db.query(Profesor).filter(Profesor.id == profesor_id).first()

def get_profesores(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Profesor).offset(skip).limit(limit).all()

def create_profesor(db: Session, profesor: ProfesorCreate):
    profesor_db = Profesor(
      nombres=profesor.nombres,
      apellidos=profesor.apellidos,
      horasClase=profesor.horasClase,
      numeroEmpleado=profesor.numeroEmpleado
    )

    db.add(profesor_db)
    db.commit()
    db.refresh(profesor_db)
    return profesor_db

def edit_profesor(db: Session, profesor_id: int, profesor: ProfesorCreate):
  put_profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()

  put_profesor.nombres = profesor.nombres
  put_profesor.apellidos = profesor.apellidos
  put_profesor.horasClase = profesor.horasClase
  put_profesor.numeroEmpleado = profesor.numeroEmpleado

  db.commit()
  db.refresh(put_profesor)

  return put_profesor

def delete_profesor(db: Session, profesor_id: int):
  profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()

  db.delete(profesor)
  db.commit()

  return profesor