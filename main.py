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

# inventory controllers

@app.get('/get/inventory/{id}')
def get(id:int, session:Session=Depends(getSession)):
    book = session.query(models.Inventory).get(id)
    return book

@app.get('/get/inventory')
def get(session: Session = Depends(getSession)):
    books = session.query(models.Inventory).all()
    return books
    
@app.post('/add/inventory')
def post(book:schemas.Inventory, session: Session = Depends(getSession)):
    book = models.Inventory(bookName=book.bookName, quantity=book.quantity)
    session.add(book)
    session.commit()
    session.refresh(book)
    
    return book

@app.put('/update/inventory/{id}')
def put(id:int, book:schemas.Inventory, session: Session = Depends(getSession)):
    bookObj = session.query(models.Inventory).get(id)
    bookObj.bookName = book.bookName
    bookObj.quantity = book.quantity
    
    session.commit()
    return bookObj