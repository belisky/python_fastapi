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


class Trainer:
    first_name=str
    last_name=str
    middle_name=Optional[str]
    email=str
    gender=str
    cohort=Optional[str]
    role=Role.trainer
    course=Courses
         