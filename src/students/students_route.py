from typing import Optional, List
from fastapi import APIRouter
from permission_request.src.students import students_model
from src.students.students_schema import Student

students_router = APIRouter(prefix="/students")

@students_router.get("/")
async def get_all_students(limit: Optional[int] = 10, offset: Optional[int] = 0):
    return await students_model.get_all_students(limit, offset)

@students_router.get("/{email}")
async def get_student_by_email(email: str):
    return await students_model.get_student_by_email(email)

@students_router.post("/")
async def insert_student(student: Student):
    return await students_model.insert_student(student)