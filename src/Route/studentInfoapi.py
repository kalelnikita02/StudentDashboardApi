from fastapi import APIRouter,Body, HTTPException
from pydantic import BaseModel
from typing import Dict

app = APIRouter()

# Sample initial data
student_info = {}

class Student(BaseModel):
    name: str = Body(...)
    email: str = Body(...)
    phone: str = Body(...)
    address: str = Body(...)

# Create operation
@app.post("/students/")
def create_student(student: Student):
    student_id = len(student_info) + 1
    student = Student(name=student.name, email=student.email, phone=student.phone, address=student.address)
    student_info[student_id] = student
    return {"id": student_id, **student.dict()}

# # Read operation
# @app.get("/students/{student_id}")
# def read_student(student_id: int):
#     if student_id not in student_info:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return student_info[student_id]

# Update operation
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in student_info:
        raise HTTPException(status_code=404, detail="Student not found")
    student_info[student_id] = student
    return {"id": student_id, **student.dict()}

# Delete operation
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in student_info:
        raise HTTPException(status_code=404, detail="Student not found")
    del student_info[student_id]
    return {"message": "Student deleted"}

# Get all students
@app.get("/students/")
def get_all_students():
    return student_info
