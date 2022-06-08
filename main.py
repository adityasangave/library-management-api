from fastapi import FastAPI, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 
from sqlalchemy import func, desc

Base.metadata.create_all(engine)
def getSession():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

# book controllers
@app.get('/issue/book')
def get(session:Session=Depends(getSession)):
    issuedBooks = session.query(models.Books).all()
    return issuedBooks

def updateInventory(session, id, operation):
    bookObj = session.query(models.Inventory).get(id)
    if operation=="borrow":
        bookObj.quantity = bookObj.quantity-1
        
        session.commit()
    else:
        bookObj.quantity = bookObj.quantity+1
        
    session.commit()
    
@app.post('/issue/book/{rollNo}/{bookName}')
def post(rollNo:int, bookName:str,session:Session=Depends(getSession)):
    bookQuery = session.query(models.Inventory).filter(models.Inventory.bookName==bookName).first()
    if bookQuery.quantity > 0:
        studentQuery = session.query(models.Books).filter(models.Books.assignedTO==rollNo).all()
        if len(studentQuery) < 3:
            issue = models.Books(bookName=bookName, assignedTO =rollNo, bookId=bookQuery.id)
            session.add(issue)
            session.commit()
            session.refresh(issue)
            
            updateInventory(session, bookQuery.id, "borrow")
        else:
            return JSONResponse({'Limit Reacehed': 'Student have already borrowed 3 books'})
    else:
        return Response("Sorry, The book is not available")
    return issue

@app.delete('/receive/book/{rollNo}/{bookName}')
def delete(rollNo:int, bookName:str,session:Session=Depends(getSession)):
    issuedBook = session.query(models.Books).filter(models.Books.assignedTO==rollNo).filter(models.Books.bookName==bookName).first()
    if issuedBook:
        updateInventory(session, issuedBook.id, "receive")
        
        session.delete(issuedBook)
        session.commit()
    else:
        return Response("Oops, Some error occured")
        
    return issuedBook

# register Student
@app.post('/add/student/')
def post(student:schemas.Student, session:Session=Depends(getSession)):
    student=models.Student(rollNo=student.rollNo, name=student.name, standard= student.standard, email=student.email)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@app.get('/all/students')
def get(session:Session=Depends(getSession)):
    students = session.query(models.Student).all()
    return students

# inventory controllers

@app.get('/get/inventory/{bookName}')
def get(bookName:str, session:Session=Depends(getSession)):
    book = session.query(models.Inventory).filter(models.Inventory.bookName==bookName).first()
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

@app.put('/update/inventory/{bookName}')
def put(bookName:str, book:schemas.updateInventory, session: Session = Depends(getSession)):
    bookObj = session.query(models.Inventory).filter(models.Inventory.bookName==bookName).first()
    bookObj.quantity = book.quantity
    
    session.commit()
    return bookObj
