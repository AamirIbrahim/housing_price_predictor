def add_extracurricular(student_id, extracurricular):
    extracurricular_record = session.query(Extracurricular).filter_by(student_id=student_id, extracurricular=extracurricular).first()

    if not extracurricular_record:
        new_ec = Extracurricular(student_id=student_id, extracurricular=extracurricular)
        session.add(new_ec)

    session.commit()
