from datetime import datetime, timedelta

def tomorrow(date=None):
    if not date:
        date = datetime.now().date()
    tomorrow = date + timedelta(1)
    return tomorrow