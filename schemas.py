from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class Create_Employee(BaseModel):
    Employee_ID: int
    Employee_Name: str
    Email: str 
    Phone_Number: str
    Department: str
    Designation: str
    Salary: float
    Joining_Date: date

class Update_Employee(BaseModel):
    Employee_Name: Optional[str] = None
    Email: Optional[str] = None
    Phone_Number: Optional[str] = None
    Department: Optional[str] = None
    Designation: Optional[str] = None
    Salary: Optional[float] = None
    Joining_Date: Optional[date] = None

class Employee(Create_Employee):
    model_config = ConfigDict(from_attributes=True)