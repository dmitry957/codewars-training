def is_divisible(*args):
    if not args: return True
    return all(args[0] % args[i] == 0 for i in range(1, len(args)))