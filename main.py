import os
import pandas as pd
from datetime import datetime, timedelta
from utils import load_data, save_data, total_bills_due
from bill_manager import add_bill, edit_bill, delete_bill
from payday_manager import calculate_next_payday

def get_user_input(prompt: str) -> str:
    """Safely get user input with a prompt."""
    return input(prompt)

def main():
    name = get_user_input("What Is Your Name: ")
    file_name = f"{name}.csv"
    
    Bill = load_data(file_name)

    print("Hello", name)
    add_info = get_user_input("Do You Need To Add Any Information? (yes/no): ").lower()
    
    if add_info == 'yes':
        payday_day = get_user_input("What day of the week is your payday? ")
        payday_frequency = get_user_input("Is your payday Weekly, Bi-Weekly, or Monthly? ").strip().lower()
        
        Bill['Payday Day'] = payday_day
        Bill['Payday Frequency'] = payday_frequency

        while True:
            print("\nCurrent Data:")
            print(Bill)
            action = get_user_input("\nWould you like to 'add', 'edit', 'delete', or 'exit'? ")

            if action.lower() == 'add':
                Bill = add_bill(Bill)
            elif action.lower() == 'edit':
                Bill = edit_bill(Bill)
            elif action.lower() == 'delete':
                Bill = delete_bill(Bill)
            elif action.lower() == 'exit':
                save_data(Bill, file_name)
                print(f"Data saved as {file_name}. Exiting the editor.")
                break
            else:
                print("Invalid action. Please choose 'add', 'edit', 'delete', or 'exit'.")

    if 'Payday Day' in Bill and not Bill['Payday Day'].isnull().all():
        payday_day = Bill['Payday Day'].iloc[0]
        payday_frequency = Bill['Payday Frequency'].iloc[0]
        next_payday = calculate_next_payday(payday_day, payday_frequency)

        Bill['Date'] = pd.to_datetime(Bill['Date'], errors='coerce')

        upcoming_bills = Bill[(Bill['Date'] >= datetime.now()) & (Bill['Date'] <= next_payday)]
        total_bills = total_bills_due(upcoming_bills) if not upcoming_bills.empty else 0

        remaining_days = (next_payday - datetime.now()).days
        print(f"There are {remaining_days} days left until your next payday.")
        

        today = datetime.now()
        end_date = today + timedelta(days=7)
        upcoming_bills_7_days = Bill[(Bill['Date'] >= today) & (Bill['Date'] <= end_date)]

        print("\nUpcoming Bills for the Next 7 Days:")
        if not upcoming_bills_7_days.empty:
            print(upcoming_bills_7_days[['Date', 'Merchant', 'Amount']])
            print(f"Total bills until next payday: ${total_bills:.2f}")
            print(f"Total amount due for upcoming bills in the next 7 days: ${total_bills_due(upcoming_bills_7_days):.2f}")
        else:
            print("No upcoming bills in the next 7 days.")

        while True:
            try:
                last_paycheck = float(get_user_input("How much was your last paycheck? "))
                difference = last_paycheck - total_bills
                if difference >= 0:
                    print(f"You will have ${difference:.2f} left after paying your bills.")
                else:
                    print(f"You will be short ${-difference:.2f} after your bills.")
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for your last paycheck.")

if __name__ == "__main__":
    main()
