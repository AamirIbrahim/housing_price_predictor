import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sample_queries.models import Students, Students_GPA, ExtraCurricular
from sqlalchemy.orm import joinedload


def get_student_by_username(session, username):
    student = session.query(Students).filter_by(username = username).first()
    return student

def get_students_in_extracurricular_with_gpa_below(session, threshold):
    results = session.query(Students.first_name,
                            Students.last_name, 
                            Students_GPA.GPA, 
                            ExtraCurricular.extracurricular
    ).join (Students_GPA, Students.student_id == Students_GPA.student_id).join(
        ExtraCurricular, Students.student_id == ExtraCurricular.student_id
    ).filter(Students_GPA.GPA < threshold).all()

    return results

def get_students_with_gpa_below(session, threshold):
    results = session.query(Students.username, 
                            Students_GPA.GPA
    ).join(
        Students_GPA, Students.student_id == Students_GPA.student_id
    ).filter(Students_GPA.GPA < threshold).all()

    return results
