from sqlalchemy import Column, Integer, String, Float

from db_app.database import Base

class Alumno(Base):
  __tablename__ = "alumnos"

  id = Column(Integer, primary_key=True, index=True)

  nombres = Column(String)
  apellidos = Column(String)
  matricula = Column(String)
  promedio = Column(Float)
  fotoPerfilUrl = Column(String, nullable=True)
