from pydantic import BaseModel,EmailStr
from typing import List

class Inventory(BaseModel):
    bookName : str
    quantity : int
    
class updateInventory(BaseModel):
    quantity : int

class Books(BaseModel):
    bookName:str
    assignedTo:int
    bookId:int
    
    class Config:
        orm_mode = True
        
class issueBook(Books):
    pass

class receiveBook(Books):
    pass
        
class Student(BaseModel):
    rollNo:int
    name:str
    standard:int
    email:EmailStr
        
class BooksList(Books):
    assignedTo: int
    students = Student
    
    class Config:
        orm_mode = True