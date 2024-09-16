"""
The operations script that contains all the database CRUD operations.
C - Create
R - Read
U - Update (** Not using update over here) 
D - Delete (** Not using delete over here)
"""
import sqlite3 as db
import os
from datetime import datetime
from datetime import timezone
from datetime import timedelta


# Defining the static variables needed.
DATABASE_FOLDER_NAME = 'database'
DATABASE_NAME = 'users.db'
PATH = os.path.join(DATABASE_FOLDER_NAME, DATABASE_NAME)


def create_database_folder():
    """
    This function creates the database folder if the folder is currently not present.
    """
    if not os.path.isdir(DATABASE_FOLDER_NAME):
        print('Creating database folder')
        os.makedirs(DATABASE_FOLDER_NAME)
        print('Database folder created')


def create_database():
    """
    This function creates the database file if the file is not currently present.
    """
    connection = db.connect(PATH)
    db_create_status = connection.total_changes
    connection.close()
    if db_create_status == 0:
        print('Database creation successful')
    else:
        print('Database creation unsuccessful')


def create_db_schema():
    """
    This function defines the table schema.
    """
    connection = db.connect(PATH)
    cursor = connection.cursor()
    query = """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                history DATETIME
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
    """
    This function gets the current date and time.
    """
    current_date_and_time = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    formatted_time = current_date_and_time.strftime('%Y-%m-%d %H:%M:%S%z')
    return formatted_time

def write_to_database(username, password, current_date_and_time):
    """
    This function is saving the user data in the database.
    """
    connection = db.connect(PATH)
    cursor = connection.cursor()
    message = ''
    query = """INSERT INTO users (username, password, history) VALUES (?, ?, ?);"""
    try:
        cursor.execute(query, (username, password, current_date_and_time))
        connection.commit()
        message = f"User `{username}` is saved in the Database."
    except Exception as exception_message:
        print(f'write_to_database: {exception_message}')
        if 'UNIQUE' in str(exception_message):
            message = f"User `{username}` already exists in the Database."
        else:
            message = "Some error has occured!"
    finally:
        print(message)
        connection.close()
    return message


def save_to_database(username, password):
    """
    This function gets the current date and time and write the user information 
    in the database.
    """
    current_date_and_time = get_current_date_and_time()
    db_response = write_to_database(username, password, current_date_and_time)
    return db_response

def initialize():
    """
    This function invokes other function which creates the database folder if not found,
    creates the database file if not present, creates the table schema.
    """
    create_database_folder()
    create_database()
    create_db_schema()


def fetch_all_user_details_from_database():
    """
    This function fetches all the user details that are present in the database
    and returns it to the frontend for the end user to see.
    """
    connection = db.connect(PATH)
    cursor = connection.cursor()
    data_dict = []
    query = """SELECT username, history FROM users;"""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        data_dict = [{"username": item[0], "datetime": item[1]} for item in rows]
    except Exception as exception_message:
        print(f"Error fetching records: {exception_message}")
    finally:
        connection.close()
    return data_dict

if __name__ == '__main__':
    save_to_database('Bob78', '123')
    fetch_all_user_details_from_database()
