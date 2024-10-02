from typing import List, Optional
from src.commons.postgres import database
from src.students.students_schema import Student

async def get_student_by_email(email: str) -> Optional[Student]:
    query = "SELECT first_name, email FROM students WHERE email = $1"
    async with database.pool.acquire() as connection:
        row = await connection.fetchrow(query, email)
        if row is not None:
            student = Student(id=row["id"],first_name=row["first_name"], email=row["email"]) 
            return student
        return None

async def get_all_students(limit: int, offset: int) -> List[Student]:
    query = "SELECT first_name, email FROM students LIMIT $1 OFFSET $2"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query, limit, offset)
        students = [Student(id=record["id"],first_name=record["first_name"], email=record["email"]) for record in rows]
        return students
    
async def insert_student(student: Student):
    query = "INSERT INTO students (first_name,last_name,middle_name,email,gender,cohort,role,course,trainer_id) VALUES ($1, $2 ,$3, $4, $5, $6, $7, $8, $9)"
    async with database.pool.acquire() as connection:
        await connection.execute(query, student.first_name, student.last_name,student.middle_name,student.email,student.gender,student.cohort,student.role,student.course,student.trainer_id)
        # inserted_id= await connection.fetchone()[0]
        
    return {"Message":"Student created."}

async def bulk_insert_students(students: List[Student]):
    query = "INSERT INTO students (first_name,last_name, email) VALUES ($1, $2)"
    user_tuples = [(student.first_name,student.last_name, student.email) for student in students]
    async with database.pool.acquire() as connection:
        await connection.executemany(query, user_tuples)

# async def create_student_table():
#     query="CREATE TABLE IF NOT EXISTS students (fn VARCHAR(50),ln VARCHAR(50),mn VARCHAR(50), email VARCHAR(50) PRIMARY KEY,gender VARCHAR(10) NULL,cohort VARCHAR(20) NULL,role VARCHAR(20) NULL,course VARCHAR(20) NULL,trainer_id VARCHAR(20) NOT NULL );"
