from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


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


class Student(BaseModel):
    id: Optional[UUID]=uuid4()
    first_name: str
    last_name: str
    middle_name=Optional[str]
    gender=Gender
    role=Role
    course=Courses[str]
    trainer=Trainer

class Trainer(BaseModel):
    id: Optional[UUID]=uuid4()
    first_name: str
    last_name: str
    middle_name=Optional[str]
    gender=Gender
    role=Role
    certificates=Certificates
    student=Student
