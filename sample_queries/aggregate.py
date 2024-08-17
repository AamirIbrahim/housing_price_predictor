import pandas as pd
from sqlalchemy import create_engine, select, func
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

count_statement = select(ExtraCurricular.extracurricular, func.count(Students.username)).\
    join(ExtraCurricular, ExtraCurricular.student_id == Students.student_id).\
    where(Students.username.like('_A%')).\
    group_by(ExtraCurricular.extracurricular).\
    order_by(func.count(Students.username).desc())
result_count = pd.DataFrame(session.execute(count_statement), columns=['extracurricular','count'])
print(result_count)

average_GPA = select(ExtraCurricular.extracurricular, func.avg(Students_GPA.GPA)).\
    join(ExtraCurricular, ExtraCurricular.student_id == Students_GPA.student_id).\
    group_by(ExtraCurricular.extracurricular)

result_average = pd.DataFrame(session.execute(average_GPA), columns=['extracurricular','average'])
print(result_average)
