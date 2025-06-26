import re

def validate_time(time):
    return bool(re.fullmatch(r'^([0-9]{1}|[0-1]{1}[0-9]{1}|2[0-3])\:[0-5]{1}[0-9]{1}', time))