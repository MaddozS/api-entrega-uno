from fastapi import APIRouter

from api import alumnos, profesores


api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
api_router.include_router(profesores.router, prefix="/profesores", tags=["profesores"])