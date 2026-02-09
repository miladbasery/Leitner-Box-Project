# auth.py
from db import get_db_connection
from utils import clear_screen, wait_for_user

#ثبت نام
def register():
    print("===|Register|===\n")
    """get username from user"""
    while True:
        username = input("Please Enter a username:")
        if not username:
            print("Error: username can not be Empty!")
            wait_for_user()
            clear_screen()
            continue

        """Check if username exists in database"""
        try:
            t_conn = get_db_connection()
            if not t_conn:
                print("Can not connect to database")
                wait_for_user()
                return None
            t_cur = t_conn.cursor()
            t_cur.execute ("SELECT id FROM users where username = %s",(username,))
            if t_cur.fetchone():
                print("usernname already exist! please try another")
                wait_for_user()
                clear_screen()
                continue
            else:
                break

        except Exception as e:
            print(f"database Error: {e}")
            wait_for_user()
            return None

        finally:
            if t_cur:
                t_cur.close()
            if t_conn:
                t_conn.close()

    """Get password from user"""
    while True:
        password = input("Please Enter a password:")
        if not password:
            print("Error: password can not be Empty!")
            wait_for_user()
            clear_screen()
            continue
        break
    clear_screen()

    """Save username and password in database"""
    try:
        conn = get_db_connection()
        if not conn:
                print("Can not connect to database")
                wait_for_user()
                return None
        cur = conn.cursor()
        cur.execute ("INSERT INTO users (username, password) VALUES (%s, %s)",(username, password))
        conn.commit()
        print(f"Registration successful! Welcome, {username}")

    except Exception as e:
        print(f"database Error: {e}")
        wait_for_user()
        return None
    
    finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    wait_for_user()

#ورود
def login():
    print("===|Login|===\n")
    """Get username and password from user"""
    while True:
        username = input("Please Enter your username:")
        if not username:
            print("Error: username can not be Empty!")
            wait_for_user()
            clear_screen()
            continue
        break
    while True:
        password = input("Please Enter a password:")
        if not password:
            print("Error: password can not be Empty!")
            wait_for_user()
            clear_screen()
            continue
        break

    """Check if username and password exist in database and return user_id to dashboard"""
    try:
        te_conn = get_db_connection()
        if not te_conn:
            print("Can not connect to database")
            wait_for_user()
            return None
        te_cur = te_conn.cursor()
        te_cur.execute ("SELECT id FROM users where username = %s and password = %s",(username,password))
        result = te_cur.fetchone()
        if result:
            print(f"login successful! Welcome {username}")
            wait_for_user()
            clear_screen()
            user_id = result[0]
            return user_id
        else:
            print("username or password is not correct!")
            print("\n==============")
            print("(1) try again!")
            print("(2) Return to main menu\n")
            choice = input("Select your choice:")
            if choice == "2":
                return None
            else:
                return login()

    except Exception as e:
        print(f"database Error: {e}")
        wait_for_user()
        return None
    
    finally:
        if te_cur:
            te_cur.close()
        if te_conn:
            te_conn.close()
   