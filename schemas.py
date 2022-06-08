from pydantic import BaseModel,EmailStr

class Inventory(BaseModel):
    bookName : str
    quantity : int
    
class Student(BaseModel):
    rollNo:int
    name:str
    standard:int
    email:EmailStr

class Books(BaseModel):
    bookName:str
    assignedTo:int
    bookId:int