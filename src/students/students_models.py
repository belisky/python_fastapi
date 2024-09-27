from typing import List, Optional
from src.commons.postgres import database
from src.students.students_schema import Student

async def get_student_by_email(email: str) -> Optional[Student]:
    query = "SELECT name, email FROM students WHERE email = $1"
    async with database.pool.acquire() as connection:
        row = await connection.fetchrow(query, email)
        if row is not None:
            student = Student(name=row["name"], email=row["email"]) 
            return student
        return None

async def get_all_students(limit: int, offset: int) -> List[Student]:
    query = "SELECT name, email FROM students LIMIT $1 OFFSET $2"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query, limit, offset)
        students = [Student(name=record["name"], email=record["email"]) for record in rows]
        return students