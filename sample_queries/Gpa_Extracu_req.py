def get_students_below_gpa_threshold(threshold=3.0):
    # Query to find students who are in extracurriculars and have a GPA below the threshold
    students = session.query(Student.first_name, Student.last_name)\
                      .join(StudentGPA, Student.student_id == StudentGPA.student_id)\
                      .join(Extracurricular, Student.student_id == Extracurricular.student_id)\
                      .filter(StudentGPA.gpa < threshold)\
                      .all()
    
    return students
