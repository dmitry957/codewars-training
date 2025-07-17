import re
def search_names(logins):
    return [pair for pair in filter(lambda l: bool(re.search(r'_$', l[0])), logins)]