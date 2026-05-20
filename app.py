import pymysql
from flask import Flask, g
from config import Config

class MySQL:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.teardown_appcontext
        def close_db(error):
            db = g.pop('mysql_db', None)
            if db is not None:
                db.close()

    @property
    def connection(self):
        if 'mysql_db' not in g:
            from flask import current_app
            host = current_app.config.get('MYSQL_HOST', 'localhost')
            user = current_app.config.get('MYSQL_USER', 'root')
            password = current_app.config.get('MYSQL_PASSWORD', '')
            database = current_app.config.get('MYSQL_DB')
            
            try:
                g.mysql_db = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            except pymysql.err.OperationalError as e:
                if e.args[0] == 1049:  # Unknown database 'quiz_db'
                    # Connect without database first
                    temp_conn = pymysql.connect(host=host, user=user, password=password)
                    cursor = temp_conn.cursor()
                    
                    # Create database
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                    cursor.execute(f"USE `{database}`")
                    
                    # Read and import quiz_db.sql
                    import os
                    sql_path = os.path.join(current_app.root_path, 'quiz_db.sql')
                    if os.path.exists(sql_path):
                        with open(sql_path, 'r', encoding='utf-8') as f:
                            sql_content = f.read()
                        
                        statement = ""
                        for line in sql_content.splitlines():
                            trimmed = line.strip()
                            if not trimmed or trimmed.startswith('--') or trimmed.startswith('#'):
                                continue
                            if trimmed.startswith('/*') and trimmed.endswith('*/'):
                                continue
                            statement += line + "\n"
                            if trimmed.endswith(';'):
                                try:
                                    cursor.execute(statement)
                                except Exception:
                                    pass
                                statement = ""
                    temp_conn.commit()
                    temp_conn.close()
                    
                    # Reconnect now that the database exists
                    g.mysql_db = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                    )
                else:
                    raise e
        return g.mysql_db

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5001)
