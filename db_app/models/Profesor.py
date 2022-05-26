from sqlalchemy import Column, Integer, String

from db_app.database import Base

class Profesor(Base):
  __tablename__ = "profesores"

  id = Column(Integer, primary_key=True, index=True)

  nombres = Column(String)
  apellidos = Column(String)
  horasClase = Column(Integer)
  numeroEmpleado = Column(Integer)
  
