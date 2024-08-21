pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)

    # Relationships
    gpa = relationship("StudentGPA", cascade="all, delete", back_populates="student")
    extracurriculars = relationship("Extracurricular", cascade="all, delete", back_populates="student")

class StudentGPA(Base):
    __tablename__ = 'students_gpa'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    gpa = Column(Float, nullable=False)

    # Relationships
    student = relationship("Student", back_populates="gpa")

class Extracurricular(Base):
    __tablename__ = 'extracurricular'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    extracurricular = Column(String(100), primary_key=True)

    # Relationships
    student = relationship("Student", back_populates="extracurriculars")

# Set up the engine and session
engine = create_engine('sqlite:///school.db')  # Use your database URL here
Session = sessionmaker(bind=engine)
session = Session()
