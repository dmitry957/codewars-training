def is_lucky(ticket):
    if len(ticket) != 6 or not ticket.isdigit():
        return False
    digits = list(map(int, ticket))
    mid = len(digits) // 2
    return sum(digits[:mid]) == sum(digits[mid:])