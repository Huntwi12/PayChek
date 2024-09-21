import pandas as pd
import os
from datetime import datetime, timedelta

def load_data(file_name):
    if os.path.isfile(file_name):
        return pd.read_csv(file_name, parse_dates=['Date'])
    return pd.DataFrame(columns=['Date', 'Merchant', 'Amount', 'Frequency', 'Payday Day', 'Payday Frequency'])

def save_data(data, file_name):
    data.to_csv(file_name, index=False)

def calculate_next_payday(payday_day, payday_frequency):
    today = datetime.now()
    days_ahead = (list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).index(payday_day) - today.weekday() + 7) % 7

    if payday_frequency == 'weekly':
        return today + timedelta(days=days_ahead)
    elif payday_frequency == 'bi-weekly':
        return today + timedelta(days=days_ahead + 14)
    elif payday_frequency == 'monthly':
        return today + timedelta(days=(30 - today.day + days_ahead) % 30)

def total_bills_due(bill_data):
    return bill_data['Amount'].sum()
