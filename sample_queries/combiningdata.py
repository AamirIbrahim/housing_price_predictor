import pandas as pd
from sqlalchemy import create_engine, select, func
from sqlalchemy.pool import NullPool
import os
import load_dotenv
from models import Students, Students_GPA, ExtraCurricular
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv.load_dotenv()

# Database connection setup
connect_args = {'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']),
                       connect_args=connect_args, poolclass=NullPool)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example 1: Counting students in each extracurricular activity
count_statement = select(ExtraCurricular.extracurricular, func.count(Students.username)).\
    join(ExtraCurricular, ExtraCurricular.student_id == Students.student_id).\
    group_by(ExtraCurricular.extracurricular).\
    order_by(func.count(Students.username).desc())

# Execute the query and load it into a DataFrame
result_count = pd.DataFrame(session.execute(count_statement), columns=['extracurricular', 'student_count'])
print("Count of students in each extracurricular activity:")
print(result_count)

# Example 2: Calculating the average GPA by extracurricular activity
average_GPA = select(ExtraCurricular.extracurricular, func.avg(Students_GPA.GPA)).\
    join(ExtraCurricular, ExtraCurricular.student_id == Students_GPA.student_id).\
    group_by(ExtraCurricular.extracurricular)

# Execute the query and load it into a DataFrame
result_average = pd.DataFrame(session.execute(average_GPA), columns=['extracurricular', 'average_GPA'])
print("\nAverage GPA by extracurricular activity:")
print(result_average)

# Example 3: Calculating the total number of extracurricular activities each student is involved in
activity_count_per_student = select(Students.username, func.count(ExtraCurricular.extracurricular)).\
    join(ExtraCurricular, ExtraCurricular.student_id == Students.student_id).\
    group_by(Students.username).\
    order_by(func.count(ExtraCurricular.extracurricular).desc())

# Execute the query and load it into a DataFrame
result_activity_count = pd.DataFrame(session.execute(activity_count_per_student), columns=['username', 'activity_count'])
print("\nTotal number of extracurricular activities each student is involved in:")
print(result_activity_count)

# Example 4: Combining the results (optional demonstration)
combined_results = pd.merge(result_count, result_average, on='extracurricular', how='inner')
print("\nCombined results of student count and average GPA by extracurricular activity:")
print(combined_results)

# Example 5: Further combining with individual student activity count
# To merge student activity count with extracurricular activities, we first need to pivot the activity count DataFrame
pivot_activity_count = result_activity_count.pivot_table(index='username', values='activity_count')

# Merging the pivoted DataFrame with combined results
final_combined_results = combined_results.merge(pivot_activity_count, left_on='extracurricular', right_index=True, how='inner')
print("\nFinal combined results with student activity counts:")
print(final_combined_results)
