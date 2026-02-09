# cards.py
from datetime import datetime
from db import get_db_connection
from utils import clear_screen, wait_for_user

def add_card(user_id):
    clear_screen()
    print("=== ADD CARD ===")
    print("Format: Question :: Answer")
    entry = input("Enter card info: ")
    
    if "::" in entry:
        q, a = entry.split("::", 1)
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cards (user_id, question, answer, slot, last_review_date) VALUES (%s, %s, %s, 1, %s)",
            (user_id, q.strip(), a.strip(), datetime.now().date())
        )
        conn.commit()
        cur.close()
        conn.close()
        print("Card added to Slot 1.")
    else:
        print("Invalid format. Use '::' separator.")
    wait_for_user()

def modify_card(user_id):
    clear_screen()
    print("=== MODIFY CARD ===")
    slot = input("Select Slot (1-6): ")
    if not slot.isdigit(): return
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, question, answer FROM cards WHERE user_id = %s AND slot = %s", (user_id, slot))
    cards = cur.fetchall()
    
    if not cards:
        print("No cards in this slot.")
        wait_for_user()
        return

    for idx, (cid, q, a) in enumerate(cards, 1):
        print(f"[{idx}] {q} :: {a}")
        
    choice = input("\nSelect card number to modify: ")
    if choice.isdigit() and 1 <= int(choice) <= len(cards):
        selected_card = cards[int(choice)-1]
        card_id = selected_card[0]
        
        action = input("(D)elete or (E)dit? ").lower()
        if action == 'd':
            cur.execute("DELETE FROM cards WHERE id = %s", (card_id,))
            print("Card Deleted.")
        elif action == 'e':
            new_entry = input("Enter new 'Question :: Answer': ")
            if "::" in new_entry:
                nq, na = new_entry.split("::", 1)
                cur.execute("UPDATE cards SET question=%s, answer=%s WHERE id=%s", (nq.strip(), na.strip(), card_id))
                print("Card Updated.")
        conn.commit()
    
    cur.close()
    conn.close()
    wait_for_user()