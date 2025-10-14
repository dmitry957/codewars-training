def solve(st):
    stack = []
    for char in st:
        if char != ')':
            stack.append(char)
        else:
            part = []
            while stack and stack[-1] != '(':
                part.append(stack.pop())                
            stack.pop()
            part.reverse()
            inner = ''.join(part)
            repeat = ''
            while stack and stack[-1].isdigit():
                repeat = stack.pop() + repeat
            repeat = int(repeat) if repeat else 1
            stack.append(inner * repeat)
    return ''.join(stack)