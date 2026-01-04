# cards.py
from datetime import datetime
from db import get_db_connection
from utils import clear_screen, wait_for_user

def add_card(user_id):
    """
    TODO: (تسک نفر سوم)
    1. از کاربر سوال و جواب را با فرمت (Question :: Answer) بگیرید.
    2. متن را جدا کنید.
    3. در جدول cards برای این user_id ذخیره کنید.
    4. مقدار slot پیش‌فرض 1 است.
    """
    print(f"Adding card for user {user_id}... Not implemented yet.")
    wait_for_user()

def modify_card(user_id):
    """
    TODO: (تسک نفر سوم)
    1. لیست کارت‌های یک اسلات را نمایش دهید.
    2. اجازه دهید کاربر یک کارت را انتخاب کند.
    3. قابلیت حذف (Delete) یا ویرایش (Edit) را پیاده کنید.
    """
    print(f"Modifying cards for user {user_id}... Not implemented yet.")
    wait_for_user()