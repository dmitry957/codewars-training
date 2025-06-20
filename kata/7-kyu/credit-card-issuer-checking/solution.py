import re
def get_issuer(number):
    card_number = str(number)
     if bool(re.match(r'^(34)|(37)', card_number)) and len(card_number) == 15:
        return 'AMEX'
    elif bool(re.match(r'^(6011)', card_number)) and len(card_number) == 16:
        return 'Discover'
    elif bool(re.match(r'^(51)|(52)|(53)|(54)|(55)', card_number)) and len(card_number) == 16:
        return 'Mastercard'
    elif bool(re.match(r'^(4)', card_number)) and (len(card_number) == 13 or len(card_number) == 16):
        return 'VISA'
    else:
        return 'Unknown'