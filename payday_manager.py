from datetime import datetime, timedelta

def calculate_next_payday(payday_day: str, payday_frequency: str) -> datetime:
    """Calculate the next payday based on the specified day and frequency."""
    today = datetime.now()
    days_ahead = (get_day_of_week(payday_day) - today.weekday()) % 7

    if payday_frequency == 'weekly':
        next_payday = today + timedelta(days=days_ahead)
    elif payday_frequency == 'bi-weekly':
        next_payday = today + timedelta(days=days_ahead + 14)
    elif payday_frequency == 'monthly':
        next_month = today.month + 1 if today.month < 12 else 1
        next_year = today.year if next_month > 1 else today.year + 1
        next_payday = datetime(next_year, next_month, get_day_of_month(payday_day))
    else:
        raise ValueError("Invalid payday frequency. Must be 'weekly', 'bi-weekly', or 'monthly'.")

    return next_payday

def get_day_of_week(day_name: str) -> int:
    """Convert day name to its corresponding weekday number."""
    days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }
    return days.get(day_name.lower(), -1)

def get_day_of_month(day: str) -> int:
    """Extract the day of the month from a string. Assumes input is a valid integer string."""
    try:
        day_int = int(day)
        if 1 <= day_int <= 31:
            return day_int
        else:
            raise ValueError("Day must be between 1 and 31.")
    except ValueError:
        raise ValueError("Invalid day input. Please enter a valid day of the month.")
