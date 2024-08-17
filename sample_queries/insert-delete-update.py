import pandas as pd
from sqlalchemy import create_engine, select, or_, and_
from sqlalchemy.pool import NullPool
import os
import load_dotenv
from models import Students, Students_GPA, ExtraCurricular
from sqlalchemy.orm import sessionmaker

load_dotenv.load_dotenv()

connect_args={'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']), 
                       connect_args=connect_args, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()

# Insertion of a new GPA record
new_student = Students_GPA(student_id=100, GPA=3.5)
session.add(new_student)
session.commit()

# # Update the GPA of a student
update_student = session.query(Students_GPA).filter(Students_GPA.student_id == 100)
update_student.GPA = 4.0
session.commit()

# # Delete the GPA record of a student
delete_student = session.query(Students_GPA).filter(Students_GPA.student_id == 100)
session.delete(delete_student)
session.commit()