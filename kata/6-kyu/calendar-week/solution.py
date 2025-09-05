from datetime import datetime
def get_calendar_week(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return date.isocalendar()[1]