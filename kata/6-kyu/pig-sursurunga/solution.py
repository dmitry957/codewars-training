import re
def sursurungal(txt):
    def replacer(match):
        num = int(match.group(1))
        word = match.group(2)
        if num != 1 and word.endswith('s'):
            word = word[:-1]
        
        if num in (0, 1):
            return f"{num} {word}"
        elif num == 2:
            return f"{num} bu{word}"
        elif 3 <= num <= 9:
            return f"{num} {word}zo"
        else:               
            return f"{num} ga{word}ga"  
    return re.sub(r'(\d+)\s+([a-zA-Z]+)', replacer, txt)