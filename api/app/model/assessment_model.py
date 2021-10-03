from sqlalchemy import Column, Integer, String,Float
from app.database import Base


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    chargeable_income = Column(Integer)
    calculations = Column(String)
    rate = Column(Float)
    tax = Column(Integer)
