def delete_student(student_id):
    student = session.query(Student).filter_by(student_id=student_id).first()

    if student:
        session.delete(student)
        session.commit()
