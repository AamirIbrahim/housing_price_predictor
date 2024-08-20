import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import os
import load_dotenv
from models import Students, StudentsCopy
from sqlalchemy.orm import sessionmaker

load_dotenv.load_dotenv()

connect_args={'ssl': {'tls': True}}
engine = create_engine("mysql+pymysql://{0}:{1}@{2}:3306/incubator"
                       .format(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST']), 
                       connect_args=connect_args, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()

def login_method_rawSQL(user_input, user_input_password):
    
    users = session.query(Students.username, Students.password) .\
        filter(Students.username == user_input, Students.password == user_input_password)
    user_login = pd.DataFrame(users, columns=['username', 'password'])
    
    print(user_login)
    if len(user_login) > 0:
        print("Login successful")
    else:
        print("Incorrect Credentials")
    session.close()

user_input_user = "' OR 1=1; -- '"
user_input_password = "123456"

login_method_rawSQL(user_input_user, user_input_password)
