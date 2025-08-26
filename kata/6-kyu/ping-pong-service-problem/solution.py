def service(score):
    first, second = map(int, score.split(':'))
    total_score = first + second
    if first >= 20 and second >= 0:
        if ((total_score - 40) // 2) % 2 == 0:
            return 'first'
        else:
            return 'second'
    else:
        if (total_score // 5) % 2 == 0:
            return 'first'
        else:
            return 'second'