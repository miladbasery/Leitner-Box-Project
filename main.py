
import sys
from db import setup_database
from utils import clear_screen
import auth
import cards
import review

def dashboard_menu(user_id):
    while True:
        clear_screen()
        print("=== USER DASHBOARD ===")
        print("1) Show Box")
        print("2) Add Card")
        print("3) Modify Card")
        print("4) Review Cards")
        print("5) Logout")
        
        choice = input("\nSelect Option: ")
        
        if choice == '1': review.show_box(user_id)
        elif choice == '2': cards.add_card(user_id)
        elif choice == '3': cards.modify_card(user_id)
        elif choice == '4': review.review_cards(user_id)
        elif choice == '5': break

def start_menu():
    setup_database()
    while True:
        clear_screen()
        print("=== LEITNER BOX START MENU ===")
        print("1) Register")
        print("2) Login")
        print("3) Exit")
        
        choice = input("\nSelect Option: ")
        
        if choice == '1':
            auth.register()
        elif choice == '2':
            user_id = auth.login()
            if user_id:
                dashboard_menu(user_id)
        elif choice == '3':
            sys.exit()

if __name__ == "__main__":
    start_menu()