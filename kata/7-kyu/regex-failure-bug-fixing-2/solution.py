import re
def filter_words(phrase):
    return re.sub(r"(bad|mean|ugly|horrible|hideous)", "awesome", phrase, flags=re.I)