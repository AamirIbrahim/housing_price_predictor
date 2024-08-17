import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import os
import load_dotenv

load_dotenv.load_dotenv()

connect_args={'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']), 
                       connect_args=connect_args, poolclass=NullPool)

def login_method_rawSQL(user_input, user_input_password):
    print("Connected to MySQL")
    query = "SELECT username, password from students_copy WHERE username = '{0}' and password = '{1}';".format(user_input, user_input_password)
    print(query)
    df = pd.read_sql(query, con=engine)
    print(df)
    if len(df) > 0:
        print("Login successful")
    else:
        print("Incorrect Credentials")

user_input_user = "JAMESSMITH"
user_input_password = "123456"

login_method_rawSQL(user_input_user, user_input_password)
