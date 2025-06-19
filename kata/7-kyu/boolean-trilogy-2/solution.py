def calculate(expr: str, values: dict[str, int]) -> int:
    expression = ''.join(str(values.get(char, char)) for char in expr)
    return eval(expression)