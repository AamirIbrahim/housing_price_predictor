import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import os
import load_dotenv
from sqlalchemy.orm import sessionmaker

from queries.insert_operations import insert_student, insert_gpa, insert_extracurricular
from queries.select_operations import get_student_by_username, get_students_with_gpa_below
from queries.update_operations import update_gpa, update_student_password
from queries.delete_operations import delete_student, delete_extracurricular
from queries.mass_email_function import get_students_for_mass_email


load_dotenv.load_dotenv()

# Database connection setup
connect_args = {'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']),
                       connect_args=connect_args, poolclass=NullPool)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def main():

    # Insert operations
    print("Inserting records...")
    insert_student(session, 'harry_potter', 'Harry', 'Potter', 'gryffindor123')
    insert_student(session, 'naruto_uzumaki', 'Naruto', 'Uzumaki', 'RamenLover322')
    insert_gpa(session, get_student_by_username(session, 'harry_potter').student_id, 3.8)
    insert_gpa(session, get_student_by_username(session, 'naruto_uzumaki').student_id, 2.7)
    insert_extracurricular(session, get_student_by_username(session,'naruto_uzumaki').student_id, 'Basketball')
    insert_extracurricular(session, get_student_by_username(session, 'harry_potter').student_id, 'Magic Chess Club')


    # Select operations
    print(f"Selecting records...")
    student = get_student_by_username(session, 'harry_potter')
    print(f"Selected student: {student.username}, {student.password}")

    students_with_low_gpa = get_students_with_gpa_below(session, 3.0)
    print("\nStudents with GPA below 3.0:")
    for student in students_with_low_gpa:
        print(f"Student: {student.username}, GPA: {student.GPA}")

    print ("\nSending mass emails to students in extracurricular activities with GPA below 3.0")
    get_students_for_mass_email(session, 3.0)


    # Updating records
    print("\nUpdating records...")
    update_student_password(session, 'naruto_uzumaki', 'RamenLover100')
    update_gpa(session, get_student_by_username(session, 'naruto_uzumaki').student_id, 2.9)


    # Deleting operations
    print("\nDeleting records...")
    delete_extracurricular(session, get_student_by_username(session, 'harry_potter').student_id, 'Magic Chess Club')
    delete_student(session, 'harry_potter')

    
if __name__ == "__main__":
    main()

