from sqlalchemy import Column, Integer, Text
from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    name = Column(Text,primary_key=True)
    monthly_salary = Column(Integer)
