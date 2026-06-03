from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas

#  Create a new employee record
def create_employee(db: Session, employee: schemas.Create_Employee):
   
    existing_id = db.query(models.Employee).filter(
        models.Employee.Employee_ID == employee.Employee_ID
    ).first()
    if existing_id:
        raise HTTPException(status_code=400, detail="Employee ID already exists.")


    
    existing_email = db.query(models.Employee).filter(
        models.Employee.Email == employee.Email
    ).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="An employee with this email already exists.")



    db_employee = models.Employee(
        Employee_ID=employee.Employee_ID,
        Employee_Name=employee.Employee_Name,
        Email=employee.Email,
        Phone_Number=employee.Phone_Number,
        Department=employee.Department,
        Designation=employee.Designation,
        Salary=employee.Salary,
        Joining_Date=employee.Joining_Date
    )

    # Step D: Save the object to the database
    db.add(db_employee)
    db.commit() # Save changes
    db.refresh(db_employee) # Get the new ID from the database

    return db_employee


# 2. Get a list of all employees
def get_employees(db: Session):
    # Query all records from the employee_records table
    return db.query(models.Employee).all()


# 3. Find a single employee by their unique ID
def get_employee(db: Session, emp_id: int):
    employee = db.query(models.Employee).filter(
        models.Employee.Employee_ID == emp_id
    ).first()

    # If the employee is not found, raise a 404 error
    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")
    
    return employee


# 4. Update an existing employee's information
def update_employee(db: Session, emp_id: int, employee: schemas.Update_Employee):
    # Step A: Find the employee in the database
    db_employee = db.query(models.Employee).filter(
        models.Employee.Employee_ID == emp_id
    ).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")

    # Step B: Check if the new email belongs to another employee
    if employee.Email:
        existing_employee = db.query(models.Employee).filter(
            models.Employee.Email == employee.Email,
            models.Employee.Employee_ID != emp_id
        ).first()
        if existing_employee:
            raise HTTPException(status_code=400, detail="An employee with this email already exists.")

    # Step C: Update the fields that were provided
    update_data = employee.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)

    # Step D: Save changes
    db.commit()
    db.refresh(db_employee)

    return db_employee


# 5. Delete an employee record
def delete_employee(db: Session, emp_id: int):
    # Step A: Find the employee
    employee = db.query(models.Employee).filter(
        models.Employee.Employee_ID == emp_id
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found")
        
    # Step B: Remove the employee and commit changes
    db.delete(employee)
    db.commit()

    return employee