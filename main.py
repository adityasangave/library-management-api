from fastapi import FastAPI, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)
def getSession():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

# register Student
@app.post('/add/student/')
def post(student:schemas.Student, session:Session=Depends(getSession)):
    student=models.Student(rollNo=student.rollNo, name=student.name, standard= student.standard, email=student.email)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student