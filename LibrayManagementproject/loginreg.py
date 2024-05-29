def login_user(username, password):
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
