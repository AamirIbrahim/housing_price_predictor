import pandas as pd
from sqlalchemy import create_engine, select, or_, and_
from sqlalchemy.pool import NullPool
import os
import load_dotenv
from models import Students, Students_GPA, ExtraCurricular
from sqlalchemy.orm import sessionmaker

load_dotenv.load_dotenv()

connect_args={'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']), 
                       connect_args=connect_args, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()

def insert_gpa(student_id, GPA):
    """
    Insert a GPA for a new student

    :param student_id: int
    :param GPA: float

    :return: Students_GPA
    """
    student_gpa = Students_GPA(student_id=student_id, GPA=GPA)
    session.add(student_gpa)
    session.commit()
    return student_gpa

def update_gpa(student_id, GPA):
    """
    Update a GPA for an existing student 

    :param student_id: int
    :param GPA: float

    :return: student_gpa
    """
    student_gpa = session.query(Students_GPA).filter(Students_GPA.student_id == student_id).first()
    if student_gpa:
        student_gpa.GPA = GPA
    session.commit()
    return student_gpa

def delete_gpa(student_id):
    """
    Delete a GPA for a student

    :param student_id: int

    :return: student_gpa
    """
    student_gpa = session.query(Students_GPA).filter(Students_GPA.student_id == student_id).first()
    if student_gpa:
        session.delete(student_gpa)
        session.commit()
    return student_gpa

def insert_student(username, first_name, last_name, password):
    """
    Insert a new student

    :param username: str
    :param first_name: str
    :param last_name: str
    :param password: str

    :return: student
    """
    student = Students(username=username, first_name=first_name, last_name=last_name, password=password)
    session.add(student)
    session.commit()
    print('test')
    return student

def update_student(student_id, username=None, first_name=None, last_name=None, password=None):
    """
    Update a student's information

    :param student_id: int
    :param username: str
    :param first_name: str
    :param last_name: str
    :param password: str

    :return: student
    """
    student = session.query(Students).filter(Students.student_id == student_id).first()
    if student:
        if username:
            student.username = username
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if password:
            student.password = password
    session.commit()
    return student

def delete_student(student_id):
    """
    Delete a student

    :param student_id: int

    :return: student
    """
    student_in_students = session.query(Students).filter(Students.student_id == student_id).first()

    if student_in_students:
        session.delete(student_in_students)
        delete_gpa(student_id)
        delete_extra_curricular(student_id)
        session.commit()
    return student_in_students

def insert_extra_curricular(student_id, activity):
    """
    Insert an extra curricular activity for a student

    :param student_id: int
    :param activity: str

    :return: extra_curricular
    """

    extra_curricular = ExtraCurricular(student_id=student_id, activity=activity)
    session.add(extra_curricular)
    session.commit()
    return extra_curricular

def update_extra_curricular(student_id, activity):
    """
    Update a student's extra curricular activity

    :param student_id: int
    :param activity: str

    :return: extra_curricular
    """
    extra_curricular = session.query(ExtraCurricular).filter(ExtraCurricular.student_id == student_id).first()
    if extra_curricular:
        extra_curricular.activity = activity
    session.commit()
    return extra_curricular

def delete_extra_curricular(student_id):
    """
    Delete a student's extra curricular activity

    :param student_id: int

    :return: extra_curricular
    """
    extra_curricular = session.query(ExtraCurricular).filter(ExtraCurricular.student_id == student_id).first()
    if extra_curricular:
        session.delete(extra_curricular)
        session.commit()
    return extra_curricular

def mass_email():
    """
    Send a mass email to all students

    :return: email
    """
    email = session.query(Students.first_name, 
                          Students.last_name,
                          Students_GPA.GPA, 
                          ExtraCurricular.extracurricular
    ).join(Students_GPA, Students.student_id == Students_GPA.student_id
    ).join(ExtraCurricular, Students.student_id == ExtraCurricular.student_id
    ).filter(Students_GPA.GPA < 3.0).all()
    return email

print(insert_student('johndoe', 'John', 'Doe', 'password'))