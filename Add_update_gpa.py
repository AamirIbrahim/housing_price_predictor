def add_or_update_gpa(student_id, gpa):
    gpa_record = session.query(StudentGPA).filter_by(student_id=student_id).first()

    if gpa_record:
        gpa_record.gpa = gpa
    else:
        new_gpa = StudentGPA(student_id=student_id, gpa=gpa)
        session.add(new_gpa)

    session.commit()
