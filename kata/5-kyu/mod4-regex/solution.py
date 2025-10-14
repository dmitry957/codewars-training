import re

class Mod:
    mod4 = re.compile(r'.*\[[+-]?0*(?:[048]|(?:\d*(?:[02468][048]|[13579][26])))\].*')
