def hofstadter_q(n, memo={1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    memo[n] = hofstadter_q(n - hofstadter_q(n - 1, memo), memo) + hofstadter_q(n - hofstadter_q(n - 2, memo), memo)
    return memo[n]