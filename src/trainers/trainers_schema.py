# from pydantic import BaseModel
# from typing import Optional
# from enum import Enum


# class Gender(str,Enum):
#     male="male"
#     female="female"

# class Role(str,Enum):
#     student="student"
#     trainer="trainer"

# class Courses(str,Enum):
#     sa="solutions architect"
#     cp="cloud practitioner"

# class Certificates(str,Enum):
#     sa="solutions architect associate"
#     cp="cloud practitioner certified"
#     sap="solutions architect professional"


class Trainer:
    def __init__(self,first_name=None,last_name=None,middle_name=None,email=None,gender=None,id=None):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.email=email
        self.gender=gender
        
        
    def __repr__(self):
        return f'Trainer({self.id},\'{self.first_name}\',\'{self.last_name}\',\'{self.middle_name}\',\'{self.email}\',\'{self.gender}\')'