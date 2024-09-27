from pydantic import BaseModel
from typing import Optional
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
    first_name=str
    last_name=str
    middle_name=Optional[str]
    email=str
    gender=Gender
    cohort=Optional[str]
    role=Role.student
    course=Courses
    trainer_id=Optional[int]

