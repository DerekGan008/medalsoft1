from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Assignment)
def create_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.create_assignment(db=db, assignment=assignment)

@router.get("/", response_model=List[schemas.Assignment])
def read_assignments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_assignments(db, skip=skip, limit=limit)
