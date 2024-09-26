from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from fastapi import HTTPException
import asyncpg
import asyncio



class Gender(str,Enum):
    male="male"
    female="female"

class Role(str,Enum):
    student="student"
    trainer="trainer"

class Courses(str,Enum):
    sa="solutions architect"
    cp="cloud practitioner"

class Certificates(str,Enum):
    sa="solutions architect associate"
    cp="cloud practitioner certified"
    sap="solutions architect professional"



class Database:
    def __init__(self, dbname, user, password, host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        """Establish a connection to the PostgreSQL database"""
        return asyncpg.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )




class Student:
    
    def __init__(self, first_name,last_name,middle_name,email,gender,cohort,course,trainer_id):
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.email=email
        self.gender=gender
        self.cohort=cohort
        self.role=Role.student
        self.course=course
        self.trainer_id=trainer_id



    @staticmethod
    def create_table(db):
        """Create the users table"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS trainers (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                middle_name VARCHAR(100) NULL,
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                cohort VARCHAR(50) NULL,
                role VARCHAR(10) NOT NULL,
                course VARCHAR(20) NULL
                );
                
                       
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                middle_name VARCHAR(100) NULL,
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                cohort VARCHAR(50) NULL,
                role VARCHAR(10) NOT NULL,
                course VARCHAR(20) NULL,
                trainer_id VARCHAR(50) references trainers(id)
            );
        ''')
        conn.commit()
        cursor.close()
        conn.close()

    def save(self, db):
        """Save the user to the PostgreSQL database"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email) VALUES (%s, %s)
        ''', (self.username, self.email))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all(db):
        """Retrieve all users from the database"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(db, user_id):
        """Retrieve a user by ID"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    @staticmethod
    def update(db, user_id, username, email):
        """Update a user's details"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET username = %s, email = %s WHERE id = %s
        ''', (username, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(db, user_id):
        """Delete a user by ID"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

class Trainer:
    
    def __init__(self, first_name,last_name,middle_name,email,gender,cohort,course,trainer_id):
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.email=email
        self.gender=gender
        self.cohort=cohort
        self.role=Role.trainer
        self.course=course
         



    @staticmethod
    def create_table(db):
        """Create the users table"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS trainers (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                middle_name VARCHAR(100) NULL,
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                cohort VARCHAR(50) NULL,
                role VARCHAR(10) NOT NULL,
                course VARCHAR(20) NULL
                );
                
                       
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                middle_name VARCHAR(100) NULL,
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                cohort VARCHAR(50) NULL,
                role VARCHAR(10) NOT NULL,
                course VARCHAR(20) NULL,
                trainer_id VARCHAR(50) references trainers(id)
            );
        ''')
        conn.commit()
        cursor.close()
        conn.close()

    def save(self, db):
        """Save the user to the PostgreSQL database"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email) VALUES (%s, %s)
        ''', (self.username, self.email))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all(db):
        """Retrieve all users from the database"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(db, user_id):
        """Retrieve a user by ID"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    @staticmethod
    def update(db, user_id, username, email):
        """Update a user's details"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET username = %s, email = %s WHERE id = %s
        ''', (username, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(db, user_id):
        """Delete a user by ID"""
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
        cursor.close()
        conn.close()



 

# class Trainer(BaseModel):
#     id: int
#     first_name: str
#     last_name: str
#     middle_name=Optional[str]
#     gender=Gender
#     cohort=str
#     role=Role
#     certificates=Certificates
    
