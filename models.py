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

class Course(str,Enum):
    sa="solutions architect"
    cp="cloud practitioner"

class User(BaseModel):
    id: Optional[UUID]=uuid4
    first_name: str
    last_name: str
    middle_name=Optional[str]
    gender=Gender
    role=Role
    course=Course
