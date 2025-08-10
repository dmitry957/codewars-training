def read(tape, head, moves):
    if not moves:
        return ''
    result = [tape[head]]
    pos = head
    for move in moves[:-1]:
        if move == '>':
            pos += 1
        if move == '<':
            pos -= 1
        result.append(tape[pos])
    return ''.join(result)