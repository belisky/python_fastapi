 

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


class Student:  
    def __init__(self,first_name=None,last_name=None,middle_name=None,email=None,gender=None,cohort=None,role='student',course=None,id=None,trainer_id=None):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.email=email
        self.gender=gender
        self.cohort=cohort
        self.role=role
        self.course=course
        self.trainer_id=trainer_id

    def __repr__(self):
        return f'Student({self.id},\'{self.first_name}\',\'{self.last_name}\',\'{self.middle_name}\',\'{self.email}\',\'{self.gender}\',\'{self.cohort}\',\'{self.role}\',\'{self.course}\',{self.trainer_id})'