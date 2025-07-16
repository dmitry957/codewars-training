import re
def what_list_am_i_on(actions):
    return 'naughty' if len(list(filter(lambda s: bool(re.match(r'^(b|f|k)', s)), actions))) >= len(list(filter(lambda s: bool(re.match(r'^(g|s|n)', s)), actions))) else 'nice'