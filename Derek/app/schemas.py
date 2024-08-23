from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    students: List[User] = []

    class Config:
        orm_mode = True

class AssignmentBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    due_date: datetime

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int
    class_id: int

    class Config:
        orm_mode = True

class SubmissionBase(BaseModel):
    file_path: str
    remarks: Optional[str] = None
    submission_date: datetime

class SubmissionCreate(SubmissionBase):
    pass

class Submission(SubmissionBase):
    id: int
    assignment_id: int
    student_id: int

    class Config:
        orm_mode = True
