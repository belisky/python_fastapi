from typing import List, Optional
from src.commons.postgres import database
from src.students.students_schema import Student

async def get_student_by_email(email: str) -> Optional[Student]:
    query = "SELECT name, email FROM students WHERE email = $1"
    async with database.pool.acquire() as connection:
        row = await connection.fetchrow(query, email)
        if row is not None:
            student = Student(name=row["first_name"]+row["last_name"], email=row["email"]) 
            return student
        return None

async def get_all_students(limit: int, offset: int) -> List[Student]:
    query = "SELECT name, email FROM students LIMIT $1 OFFSET $2"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query, limit, offset)
        students = [Student(name=record["first_name"]+record["last_name"], email=record["email"]) for record in rows]
        return students
    
async def insert_student(student: Student):
    query = "INSERT INTO students (first_name,last_name, email) VALUES ($1, $2)"
    async with database.pool.acquire() as connection:
        await connection.execute(query, student.first_name, student.last_name,student.email)

async def bulk_insert_students(students: List[Student]):
    query = "INSERT INTO students (first_name,last_name, email) VALUES ($1, $2)"
    user_tuples = [(student.first_name,student.last_name, student.email) for student in students]
    async with database.pool.acquire() as connection:
        await connection.executemany(query, user_tuples)