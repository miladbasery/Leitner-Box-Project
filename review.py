
from datetime import datetime, timedelta
import random
from db import get_db_connection
from utils import clear_screen, wait_for_user
import config

def apply_penalty_policy(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, slot, last_review_date FROM cards WHERE user_id = %s AND slot < 6", (user_id,))
    cards = cur.fetchall()
    today = datetime.now().date()
    
    for card_id, slot, last_review in cards:
        if last_review is None: continue
        
        interval = config.BOX_INTERVALS.get(slot, 1)
        due_date = last_review + timedelta(days=interval)
        penalty_deadline = due_date + timedelta(days=2)
        
        if today > penalty_deadline:
            new_slot = max(1, slot - 1)
            cur.execute("UPDATE cards SET slot = %s, last_review_date = %s WHERE id = %s", 
                        (new_slot, today, card_id))
            
    conn.commit()
    cur.close()
    conn.close()

def show_box(user_id):
    apply_penalty_policy(user_id)
    clear_screen()
    print("=== DASHBOARD ===")
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT slot, COUNT(*) FROM cards WHERE user_id = %s GROUP BY slot", (user_id,))
    counts = dict(cur.fetchall())
    cur.close()
    conn.close()
    
    for i in range(1, 7):
        count = counts.get(i, 0)
        desc = "(Learned!)" if i == 6 else f"(Every {config.BOX_INTERVALS[i]} days)"
        print(f"Slot {i}: {count} Cards {desc}")
    
    wait_for_user()

def review_cards(user_id):
    clear_screen()
    apply_penalty_policy(user_id)
    print("=== REVIEW TIME ===")
  
    user_slot = input("\nSelect a Slot to review (1-6): ")
    if not user_slot.isdigit(): return
    user_slot = int(user_slot)
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, question, answer FROM cards WHERE user_id = %s AND slot = %s", 
                (user_id, user_slot))
    slot_cards = cur.fetchall()
    
    if not slot_cards:
        print("Slot is empty.")
        wait_for_user()
        return
        
    card = random.choice(slot_cards)
    print(f"QUESTION: {card[1]}")
    input("Press Enter for answer...")
    print(f"ANSWER: {card[2]}")
    
    if input("Did you learn this? (y/n): ").lower() == 'y':
        new_slot = user_slot + 1
        print("Moved to next slot!")
    else:
        new_slot = user_slot
        print("Remains in this slot.")
        
    cur.execute("UPDATE cards SET slot = %s, last_review_date = %s WHERE id = %s", 
                (new_slot, datetime.now().date(), card[0]))
    conn.commit()
    cur.close()
    conn.close()
    wait_for_user()