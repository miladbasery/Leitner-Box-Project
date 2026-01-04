# review.py
from db import get_db_connection
from utils import clear_screen, wait_for_user
import config

def show_box(user_id):
    """
    TODO: (تسک نفر چهارم)
    1. تعداد کارت‌های موجود در هر اسلات (1 تا 6) را از دیتابیس بشمارید.
    2. به کاربر نشان دهید (مثلاً: Slot 1: 5 cards).
    """
    print(f"Showing box for user {user_id}... Not implemented yet.")
    wait_for_user()

def review_cards(user_id):
    """
    TODO: (تسک نفر چهارم)
    1. کارت‌هایی که موعد مرورشان رسیده را پیدا کنید (با توجه به تاریخ امروز).
    2. کارت را نمایش دهید و بپرسید یاد گرفت یا نه.
    3. اگر یاد گرفت: slot = slot + 1 (تا سقف 6).
    4. اگر یاد نگرفت: در همان اسلات بماند (یا طبق سناریو برگردد).
    5. تاریخ مرور (last_review_date) را به امروز آپدیت کنید.
    """
    print(f"Reviewing cards for user {user_id}... Not implemented yet.")
    wait_for_user()