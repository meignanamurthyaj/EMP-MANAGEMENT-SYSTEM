from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os
import models
import schemas
import database
import crud

# Create tables in MySQL
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Employee Management System API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  API

@app.post("/api/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.Create_Employee, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/api/employees/", response_model=List[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db=db)

@app.get("/api/employees/{emp_id}", response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee(db=db, emp_id=emp_id)

@app.put("/api/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, employee: schemas.Update_Employee, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, emp_id=emp_id, employee=employee)

@app.delete("/api/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db=db, emp_id=emp_id)
    return {"message": "Employee deleted successfully"}



# Serve the Frontend HTML from templates directory
@app.get("/", response_class=HTMLResponse)
def read_index():
    file_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="index.html not found in templates directory")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()




@app.get("/create", response_class=HTMLResponse)
def read_create():
    file_path = os.path.join(os.path.dirname(__file__), "templates", "create.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="create.html not found in templates directory")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()



@app.get("/update", response_class=HTMLResponse)
def read_update():
    file_path = os.path.join(os.path.dirname(__file__), "templates", "update.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="update.html not found in templates directory")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()



@app.get("/search", response_class=HTMLResponse)
def read_search():
    file_path = os.path.join(os.path.dirname(__file__), "templates", "search.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="search.html not found in templates directory")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()



@app.get("/view-all", response_class=HTMLResponse)
def read_view_all():
    file_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="index.html not found in templates directory")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()