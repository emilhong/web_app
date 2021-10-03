from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.model.assessment_model import Assessment
from app.model.employee_model import Employee
from app.crud import assessment_crud as crud
from app.schema import assessment_schema as schema
from app.database import SessionLocal, engine

Assessment.metadata.create_all(bind=engine)
Employee.metadata.create_all(bind=engine)

router = APIRouter(tags=["Assessment"],prefix="/assessment")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{name}")
async def update(name: str, db: Session = Depends(get_db)):
    if len(name) < 3:
        raise HTTPException(
            status_code=404, detail=f"Minimum 3 characters for name.")
    instance = crud.get(db, name)
    if instance is None:
        raise HTTPException(
            status_code=404, detail=f"name: '{name}' not found.")
    instance = crud.calculate_tax(db, instance)
    return instance

@router.put("/")
async def update(assessment:schema.AssessmentUpdate, db: Session = Depends(get_db)):
    instance = crud.get(db, assessment.name)
    if instance is None:
        raise HTTPException(
            status_code=404, detail=f"name: {assessment.name} not found.")
    instance = crud.update(db, instance, assessment)
    return instance