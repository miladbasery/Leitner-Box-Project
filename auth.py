# auth.py
from db import get_db_connection
from utils import clear_screen, wait_for_user

def register():
    """
    TODO: (تسک نفر دوم)
    1. از کاربر username و password بگیرید.
    2. به دیتابیس وصل شوید (get_db_connection).
    3. اطلاعات را در جدول users ذخیره کنید.
    4. ارورهای احتمالی (مثل تکراری بودن یوزرنیم) را هندل کنید.
    """
    print("Function register() is not implemented yet.")
    wait_for_user()

def login():
    """
    TODO: (تسک نفر دوم)
    1. یوزرنیم و پسورد را بگیرید.
    2. چک کنید در دیتابیس وجود دارد یا خیر.
    3. اگر درست بود، id کاربر را برگردانید (return user_id).
    4. اگر غلط بود، None برگردانید.
    """
    print("Function login() is not implemented yet.")
    wait_for_user()
    return None 