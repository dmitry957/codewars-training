import re
def trump_detector(trump_speech):
    speech = trump_speech.lower()
    groups = [m.group(0) for m in re.finditer(r'([aeiou])\1*', speech)]
    if not groups:
        return 0.0
    extra = sum(len(g) - 1 for g in groups)
    return round(extra / len(groups), 2)
            