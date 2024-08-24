import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sample_queries.models import Students, Students_GPA, ExtraCurricular


def delete_student(session, username):
    student = session.query(Students).filter_by(username = username).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student {username}")
    else:
        print(f"Student {username} not found.")

def delete_extracurricular(session, student_id, extracurricular):
    extracurricular_record = session.query(ExtraCurricular).filter_by(student_id=student_id, extracurricular = extracurricular).first()
    if(extracurricular_record):
        session.delete(extracurricular_record)
        session.commit()
        print(f"Deleted extracurricular {extracurricular} for student ID {student_id}")
    else:
        print(f"Extracurricular {extracurricular} for student ID {student_id} not found.")