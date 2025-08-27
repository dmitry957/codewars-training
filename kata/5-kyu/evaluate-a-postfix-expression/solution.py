def postfix_evaluator(expr):
    stack = []
    for token in expr.split():
        if token not in ('+', '-', '*', '/'):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            match token:
                case '+': stack.append(a + b)
                case '-': stack.append(a - b)
                case '*': stack.append(a * b)
                case '/': stack.append(0 if b == 0 else int(a // b))
    return stack.pop()