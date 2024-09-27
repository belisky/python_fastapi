from typing import Optional, List
from fastapi import APIRouter
from src.students import students_models
from src.students.students_schema import Student

students_router = APIRouter(prefix="/students")

@students_router.get("/")
async def get_all_users(limit: Optional[int] = 10, offset: Optional[int] = 0):
    return await students_models.get_all_students(limit, offset)
