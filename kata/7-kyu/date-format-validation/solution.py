import re
def date_checker(date):
    return bool(re.fullmatch(r'^\d{2}\-\d{2}\-\d{4}\s\d{2}\:\d{2}$', date))