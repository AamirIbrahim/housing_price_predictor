import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sample_queries.models import Students, Students_GPA, ExtraCurricular


def update_student_password(session, username, new_password):
    student = session.query(Students).filter_by(username = username).first()
    if student:
        student.password = new_password
        session.commit()
        print(f"Updated password for {username}")
    else:
        print(f"Student {username} not found.")

def update_gpa(session, student_id, new_gpa):
    gpa_record = session.query(Students_GPA).filter_by(student_id=student_id).first()
    if gpa_record:
        gpa_record.GPA = new_gpa
        session.commit()
        print(f"Updated GPA to {new_gpa} for student ID {student_id}")
    else:
        print(f"GPA record for student ID {student_id} not found.")