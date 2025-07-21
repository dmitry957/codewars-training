import re

def detect_operator(num):
    operators = {
        'Golden Telecom': ['8039'],
        'MTS': ['8050', '8066', '8095', '8099'],
        'Life:)': ['8063', '8093'],
        'Kyivstar': ['8067', '8096', '8097', '8098'],
        'Beeline': ['8068']
    }
    for operator, prefixes in operators.items():
        pattern = rf"^({'|'.join(prefixes)})\d{{7}}$"
        if re.fullmatch(pattern, num):
            return operator
    return 'no info'