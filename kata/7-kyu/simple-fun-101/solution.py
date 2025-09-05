import datetime

def regular_months(curr_month):
    month, year = map(int, curr_month.split('-'))
    month += 1
    while True:
        if month > 12:
            month = 1
            year += 1
        date = datetime.date(year, month, 1)
        if date.weekday() == 0:
            return f'{month:02d}-{year}'
        month += 1