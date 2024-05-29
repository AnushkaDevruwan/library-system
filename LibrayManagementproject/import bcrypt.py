import bcrypt
import sqlite3

def create_connection():
    return sqlite3.connect('library.db')

def register_user(username, password, email):
    connection = create_connection()
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        cursor.execute("""def login_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                print("Login successful")
            else:
                print("Invalid username or password")
        else:
            print("Invalid username or password")
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        connection.close()

# Example usage
login_user('johndoe', 'password123')

            INSERT INTO users (username, password, email)
            VALUES (?, ?, ?)
        """, (username, hashed_password, email))
        connection.commit()
        print("User registered successfully")
    except sqlite3.IntegrityError as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        connection.close()

# Example usage
register_user('johndoe', 'password123', 'john@example.com')
