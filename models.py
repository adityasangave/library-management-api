from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType

from database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True)
    bookName = Column(String(256))
    quantity = Column(Integer)
    
class Student(Base):
    __tablename__ = "students"
      
    rollNo = Column(Integer, primary_key=True)
    name = Column(String(156))
    standard = Column(Integer)
    email = Column(EmailType)
    
class Books(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    bookName = Column(String(256))
    assignedTO = Column(Integer, ForeignKey("students.rollNo"))
    bookId = Column(Integer, ForeignKey("inventory.id"))