import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect('library.db')
        print("Connection to SQLite DB successful")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

connection = create_connection()
