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

students_all = session.query(Students.__table__.columns).\
    filter(Students.student_id < 50, Students.student_id > 20)

students_all_df = pd.DataFrame(students_all, columns=[Students.__table__.columns.keys()])
print(students_all_df)

select_statement = session.query(Students.username, Students.password).\
        filter(Students.username == 'JAMESSMITH', Students.password.like('%1%'))
result = pd.DataFrame(select_statement, columns=['username', 'password'])
print(result)

select_statement = select(Students.username, Students.password).\
        where(Students.username == 'JAMESSMITH', Students.password.like('%1%'))
result = pd.DataFrame(session.execute(select_statement), columns=['username', 'password'])
print(result)

join_statement_session = session.query(Students.username, Students_GPA.GPA, Students.password).\
    join(Students_GPA, Students_GPA.student_id == Students.student_id).\
    where(or_(Students.username == 'JAMESSMITH', Students.password.like('%1%')))
result_join_session = pd.DataFrame(join_statement_session, columns=['username', 'GPA', 'password'])
print(result_join_session)

join_statement_select = select(Students.username, Students_GPA.GPA, Students.password).\
    join(Students_GPA, and_(Students_GPA.student_id == Students.student_id, Students_GPA.GPA > 3)).\
    where(or_(Students.username == 'JAMESSMITH', Students.password.like('%1%')))
result_join_select = pd.DataFrame(session.execute(join_statement_select), columns=['username', 'GPA', 'password'])
print(result_join_select)

double_join_statement = select(Students.username, ExtraCurricular.extracurricular, Students_GPA.GPA, Students.password).\
    join(Students_GPA, Students_GPA.student_id == Students.student_id).\
    join(ExtraCurricular, and_(ExtraCurricular.student_id == Students.student_id, \
                               ExtraCurricular.student_id == Students_GPA.student_id)).\
    where(or_(Students.username == 'JAMESSMITH', Students.password.like('%1%')), \
          ExtraCurricular.extracurricular.like("%Students%"), Students_GPA.GPA > 3.0)
result_join = pd.DataFrame(session.execute(double_join_statement), columns=['username', 'extracurricular', 'GPA', 'password'])
print(result_join)