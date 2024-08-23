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

def students_table(first, last, user, passw, funct, input_id):
    if(funct == 'insert'):
        insert_student = Students(first_name = first, last_name = last, 
                                  username = user, password = passw)
        session.add(insert_student)
        session.commit()

        select_id = select(Students.student_id).\
            where(Students.username == user, Students.password == passw)
        id = session.execute(select_id).fetchone()
        print(id)

    if( funct == 'update'):
        update_student = session.query(Students).filter_by(student_id = input_id).first()
        update_student.first_name = first
        update_student.last_name = last
        update_student.username = user
        update_student.password = passw
        session.commit()
        
    if(funct == 'delete'):
        delete_student = session.query(Students).filter_by(student_id = input_id).first()
        session.delete(delete_student)
        session.commit()

    if(funct == 'delete_all'):
        delete_student = session.query(Students).filter_by(student_id = input_id).first()
        delete_gpa = session.query(Students_GPA).filter_by(student_id = input_id).first()
        delete_extra = session.query(ExtraCurricular).filter_by(student_id = input_id).first()
        session.delete(delete_student)
        session.delete(delete_gpa)
        session.delete(delete_extra)
        session.commit()

def student_gpa_table(gpa, funct, input_id):
    if(funct == 'insert'):
        insert_gpa = Students_GPA(student_id = input_id, GPA = gpa)
        session.add(insert_gpa)
        session.commit()

    if( funct == 'update'):
            update_gpa = session.query(Students_GPA).filter_by(student_id = input_id).first()
            update_gpa.GPA = gpa
            session.commit()
            
    if(funct == 'delete'):
        delete_gpa = session.query(Students_GPA).filter_by(student_id = input_id).first()
        session.delete(delete_gpa)
        session.commit()

def extra_table(extra, funct, input_id):
    if(funct == 'insert'):
        insert_extra = ExtraCurricular(student_id = input_id, extracurricular = extra)
        session.add(insert_extra)
        session.commit()

    if( funct == 'update'):
            update_extra = session.query(ExtraCurricular).filter_by(student_id = input_id).first()
            update_extra.extracurricular = extra
            session.commit()
            
    if(funct == 'delete'):
        delete_extra = session.query(ExtraCurricular).filter_by(student_id = input_id).first()
        session.delete(delete_extra)
        session.commit()


#IMPLEMENTATION OF FUNCTIONS

# students_table('Larry', 'Ebanks', 'LarBand', 'quigely123', 'insert', 531)
students_all = session.query(Students.__table__.columns).\
    filter(Students.student_id > 420)
students_all_df = pd.DataFrame(students_all, columns=[Students.__table__.columns.keys()])
print(students_all_df)


# student_gpa_table(3.8, 'insert', 531)
students_all = session.query(Students_GPA.__table__.columns).\
    filter(Students_GPA.student_id > 420)
students_all_df = pd.DataFrame(students_all, columns=[Students_GPA.__table__.columns.keys()])
print(students_all_df)


# extra_table('Larry Club','insert', 531)
students_all = session.query(ExtraCurricular.__table__.columns).\
    filter(ExtraCurricular.student_id > 420)
students_all_df = pd.DataFrame(students_all, columns=[ExtraCurricular.__table__.columns.keys()])
print(students_all_df)