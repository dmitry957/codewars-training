import re
def validate(domain):
    if len(domain) > 253 or domain.endswith('.') or '@' in domain:
        return False
    subdomains = domain.split('.')
    if len(subdomains) < 2 or len(subdomains) > 127:
        return False
    pattern = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$')
    for subdomain in subdomains:
        if not bool(re.fullmatch(pattern, subdomain)):
            return False
        
    if subdomains[-1].isdigit():
        return False
    return True