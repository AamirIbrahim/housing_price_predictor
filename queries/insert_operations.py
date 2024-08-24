import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sample_queries.models import Students, Students_GPA, ExtraCurricular


def insert_student(session, username, first_name, last_name, password):
    new_student = Students(username = username, first_name = first_name, 
                           last_name = last_name, password = password)
    session.add(new_student)
    session.commit()
    print (f"Inserted student {username}")


def insert_gpa(session, student_id, GPA):
    new_gpa = Students_GPA(student_id = student_id, GPA = GPA)
    session.add(new_gpa)
    session.commit()
    print(f"Inserted GPA {GPA} for students ID {student_id}")

def insert_extracurricular(session, student_id, extracurricular):
    new_activity = ExtraCurricular(student_id= student_id, extracurricular=extracurricular)
    session.add(new_activity)
    session.commit()
    print(f"Inserted extracurricular {extracurricular} for students ID {student_id}")




