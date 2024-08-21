def update_student(student_id, first_name=None, last_name=None, password=None):
    student = session.query(Student).filter_by(student_id=student_id).first()

    if student:
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if password:
            student.password = password

        session.commit()
