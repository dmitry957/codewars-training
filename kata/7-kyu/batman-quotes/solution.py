import re

class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        match = re.search(r'[0-9]{1}', hero)
        index = int(match.group(0)) if match else 0
        return f"{'Batman' if hero[0] == 'B' else 'Robin' if hero[0] == 'R' else 'Joker'}: {quotes[index]}"