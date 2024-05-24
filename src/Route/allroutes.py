from src.Route.studentInfoapi import app as studentapi
from fastapi import APIRouter
router = APIRouter()
router.include_router(studentapi)