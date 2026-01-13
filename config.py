import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_should_be_secret'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # sesuaikan dengan password MySQL
    MYSQL_DB = 'quiz_db'
