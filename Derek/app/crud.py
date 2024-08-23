from sqlalchemy.orm import Session
from app.models import User, Class_, Assignment, Submission
from app.schemas import UserCreate, ClassCreate, AssignmentCreate, SubmissionCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, hashed_password=user.password, role="student")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_class(db: Session, class_: ClassCreate):
    db_class = Class_(name=class_.name)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_class(db: Session, class_id: int):
    return db.query(Class_).filter(Class_.id == class_id).first()

def create_assignment(db: Session, assignment: AssignmentCreate):
    db_assignment = Assignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def get_assignments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Assignment).offset(skip).limit(limit).all()

def create_submission(db: Session, submission: SubmissionCreate):
    db_submission = Submission(**submission.dict())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission
