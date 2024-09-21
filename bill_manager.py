from datetime import datetime
def add_bill(bill_data):
    frequency = input("Does this charge occur Daily, Weekly, Bi-Weekly, 1M, 3M, 6M, or 1Y? ")
    
    day_of_month = input("Enter Day of the Month (1-31): ")
    date = datetime.now().replace(day=int(day_of_month), month=datetime.now().month, year=datetime.now().year)

    merchant = input("Enter Merchant: ")
    amount = float(input("Enter Amount: "))

    bill_data = bill_data.append({'Date': date, 'Merchant': merchant, 'Amount': amount, 'Frequency': frequency}, ignore_index=True)
    return bill_data

def edit_bill(bill_data):
    print("Select a row number to edit:")
    print(bill_data)
    row_to_edit = int(input("Enter row number (starting from 0): "))
    
    if 0 <= row_to_edit < len(bill_data):
        # Logic to edit the bill
        pass  # Implement the edit logic
    else:
        print("Invalid row number.")
    
    return bill_data

def delete_bill(bill_data):
    print("Select a row number to delete:")
    print(bill_data)
    row_to_delete = int(input("Enter row number (starting from 0): "))
    
    if 0 <= row_to_delete < len(bill_data):
        bill_data = bill_data.drop(row_to_delete).reset_index(drop=True)
        print("Entry deleted.")
    else:
        print("Invalid row number.")
    
    return bill_data
