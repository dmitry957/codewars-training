def play_pass(s, n):
    def shift_char(c, n):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + n) % 26 + base)
        return c

    def transform_char(c, idx):
        if c.isalpha():
            c = shift_char(c, n)
            if idx % 2 != 0:
                c = c.lower()
            else:
                c = c.upper()
        return c

    transformed = [transform_char(c, i) for i, c in enumerate(s)]
    for i in range(len(transformed)):
        if transformed[i].isdigit():
            transformed[i] = str(9 - int(transformed[i]))
    return ''.join(transformed)[::-1]