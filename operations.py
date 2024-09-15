import sqlite3 as db
import os

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
                password TEXT NOT NULL
            );"""
    try:
        cursor.execute(query)
        connection.commit()
        print('Table created')
    except db.OperationalError as exception_message:
        print(f'create_db_schema: {exception_message}')
    finally:
        connection.close()


def write_to_database(username, password):
    connection = db.connect(PATH)
    cursor = connection.cursor()
    query = """INSERT INTO users (username, password) VALUES (?, ?);"""
    try:
        cursor.execute(query, (username, password))
        connection.commit()
        message = f"User `{username}` is saved in the Database."
    except Exception as exception_message:
        print(f'write_to_database: {exception_message}')
        message = f"User `{username}` already exists in the Database."
    finally:
        print(message)
        connection.close()
    return message


def save_to_database(username, password):
    create_database_folder()
    create_database()
    create_db_schema()
    db_response = write_to_database(username, password)
    return db_response

if __name__ == '__main__':
    save_to_database('Bob78', '123')
