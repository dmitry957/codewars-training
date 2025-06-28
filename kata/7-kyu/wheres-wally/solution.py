import re

def wheres_wally(s):
    match = re.search(r' Wally\b', ' ' + s)
    return match.start() if match else -1