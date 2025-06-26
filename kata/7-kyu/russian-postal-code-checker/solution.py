import re
def zipvalidate(postcode):
    print(postcode)
    return bool(re.fullmatch(r'^[1-46][0-9]{5}$', postcode))