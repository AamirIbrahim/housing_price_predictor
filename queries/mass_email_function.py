import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sample_queries.models import Students, Students_GPA, ExtraCurricular
from queries.select_operations import get_students_in_extracurricular_with_gpa_below


def get_students_for_mass_email(session, threshold):
    students = get_students_in_extracurricular_with_gpa_below(session, threshold)
    for student in students:
        print(f"Email to: {student.first_name} {student.last_name}, GPA: {student.GPA}, Activity: {student.extracurricular}")