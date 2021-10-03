from pydantic import BaseModel

class AssessmentBase(BaseModel):
    name: str

class AssessmentUpdate(AssessmentBase):
    monthly_salary: int

class Assessment(AssessmentBase):
    pass

    class Config:
        orm_mode = True