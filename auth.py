# auth.py
import re
import psycopg2
from db import get_db_connection
from utils import clear_screen, wait_for_user

def validate_input(username, password):
    username_pattern = r"^[a-zA-Z0-9_]{3,20}$"
    
    if not re.match(username_pattern, username):
        print("Error: Username must be 3-20 chars (Letters, Numbers, _ only).")
        return False
        
    if len(password) < 4 or " " in password:
        print("Error: Password must be at least 4 chars and cannot contain spaces.")
        return False
        
    return True

def register():
    clear_screen()
    print("=== REGISTER ===")
    
 
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
 
    if not validate_input(username, password):
        wait_for_user()
        return 

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("Registration Successful!")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Error: Username already exists.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
    wait_for_user()

def login():
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user:
        return user[0] 
    else:
        print("Invalid credentials.")
        wait_for_user()
        return None