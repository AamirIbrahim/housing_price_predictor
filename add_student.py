def add_student(first_name, last_name, username, password, gpa=None, extracurriculars=None):
    new_student = Student(first_name=first_name, last_name=last_name, username=username, password=password)

    if gpa:
        new_student.gpa = [StudentGPA(gpa=gpa)]

    if extracurriculars:
        new_student.extracurriculars = [Extracurricular(extracurricular=ec) for ec in extracurriculars]

    session.add(new_student)
    session.commit()
    return new_student.student_id
