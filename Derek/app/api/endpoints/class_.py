from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db=db, class_=class_)

@router.get("/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class
