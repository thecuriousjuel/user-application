import sqlite3 as db
import os
from datetime import datetime
from datetime import timezone
from datetime import timedelta

DATABASE_FOLDER_NAME = 'database'
DATABASE_NAME = 'users.db'
PATH = os.path.join(DATABASE_FOLDER_NAME, DATABASE_NAME)


def create_database_folder():
    if not os.path.isdir(DATABASE_FOLDER_NAME):
        print('Creating database folder')
        os.makedirs(DATABASE_FOLDER_NAME)
        print('Database folder created')


def create_database():
    connection = db.connect(PATH)
    db_create_status = connection.total_changes
    connection.close()
    if db_create_status == 0:
        print('Database creation successful')
    else:
        print('Database creation unsuccessful')


def create_db_schema():
    connection = db.connect(PATH)
    cursor = connection.cursor()
    query = """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                savetime DATETIME
            );"""
    try:
        cursor.execute(query)
        connection.commit()
        print('Table created')
    except db.OperationalError as exception_message:
        print(f'create_db_schema: {exception_message}')
    finally:
        connection.close()

def get_current_date_and_time():
    current_date_and_time = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    formatted_time = current_date_and_time.strftime('%Y-%m-%d %H:%M:%S%z')
    return formatted_time

def write_to_database(username, password, current_date_and_time):
    connection = db.connect(PATH)
    cursor = connection.cursor()
    query = """INSERT INTO users (username, password, savetime) VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, (username, password, current_date_and_time))
        connection.commit()
        message = f"User `{username}` is saved in the Database."
    except Exception as exception_message:
        print(f'write_to_database: {exception_message}')
        if 'exists' in str(exception_message):
            message = f"User `{username}` already exists in the Database."
        else:
            message = f"Some error has occured!"
    finally:
        print(message)
        connection.close()
    return message



def save_to_database(username, password):
    create_database_folder()
    create_database()
    create_db_schema()
    current_date_and_time = get_current_date_and_time()

    db_response = write_to_database(username, password, current_date_and_time)
    return db_response

if __name__ == '__main__':
    save_to_database('Bob78', '123')
