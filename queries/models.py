from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String) 
    last_name = Column(String) 
    password = Column(String)

class StudentsCopy(Base):
    __tablename__ = 'students_copy'
    student_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String) 
    last_name = Column(String) 
    password = Column(String)

class Students_GPA(Base):
    __tablename__ = 'students_gpa'
    student_id = Column(Integer, primary_key=True)
    GPA = Column(Float)

class ExtraCurricular(Base):
    __tablename__ = 'extracurricular'
    student_id = Column(Integer, primary_key=True) 
    extracurricular = Column(String, primary_key=True)