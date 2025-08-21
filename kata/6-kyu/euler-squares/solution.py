def create_euler_square(n): ## Assume n is odd.
    latin_square1 = [[(i + j) % n + 1 for j in range(n)] for i in range(n)]
    latin_square2 = [[(i + j * 2) % n + 1 for j in range(n)] for i in range(n)]
    return latin_square1, latin_square2