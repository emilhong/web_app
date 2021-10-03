from sqlalchemy.orm import Session

from app.model.employee_model import Employee
from app.schema import assessment_schema as schema
from fastapi import HTTPException

def get(db:Session, name:str):
    return db.query(Employee).filter(Employee.name == name).first()

def update(db:Session, instance:dict, assessment:schema.AssessmentUpdate):
    assessment.name = instance.name
    if assessment.monthly_salary > 100000:
        raise HTTPException(status_code=400, detail=f"Monthly salary cannot be more than 100,000.") 
    db.query(Employee).filter(Employee.name == assessment.name).update(assessment.dict())
    db.commit()
    return HTTPException(status_code=201, detail=f"Update successfully.")

def calculate_tax(db:Session, instance: dict):
    
    yearly_salary = instance.monthly_salary * 12
    if yearly_salary > 0 and yearly_salary <= 5000:
        rate = 0
        tax = 0
    elif yearly_salary > 5000 and yearly_salary <= 20000:
        rate = 1
        tax = 0
    elif yearly_salary > 20000 and yearly_salary <= 35000:
        rate = 3
        tax = 150
    elif yearly_salary > 35000 and yearly_salary <= 50000:
        rate = 8
        tax = 600
    elif yearly_salary > 50000 and yearly_salary <= 70000:
        rate = 14
        tax = 1800
    elif yearly_salary > 70000 and yearly_salary <= 100000:
        rate = 21
        tax = 4600
    elif yearly_salary > 100000 and yearly_salary <= 250000:
        rate = 24
        tax = 10900
    elif yearly_salary > 250000 and yearly_salary <= 400000:
        rate = 24.5
        tax = 46900
    else:
        rate = 25
        tax = 83650
        
    tax_calculation = tax + (instance.monthly_salary * 2 * rate / 100)
    salary = yearly_salary * 100
    tax_payable = round(tax_calculation, 2) * 100
    return {"name": instance.name, "salary":int(salary), "tax_payable":int(tax_payable)}