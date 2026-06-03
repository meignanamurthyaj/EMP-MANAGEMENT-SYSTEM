from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Employee(Base):
    __tablename__ = "employee_records"
    Employee_ID = Column(Integer, primary_key=True, index=True)
    Employee_Name = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Phone_Number = Column(String(20), nullable=False)
    Department = Column(String(100), nullable=False)
    Designation = Column(String(100), nullable=False)
    Salary = Column(Float, nullable=False)
    Joining_Date = Column(Date, nullable=False)