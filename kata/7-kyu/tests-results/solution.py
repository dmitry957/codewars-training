def test(r):
    class_average = round(sum(r) / len(r), 3)
    marks = {
        'h': sum(mark in (9, 10) for mark in r),
        'a': sum(mark in (7, 8) for mark in r),
        'l': sum(mark <= 6 for mark in r)
    }
    result = [class_average, marks]
    if marks['h'] == len(r):
        result.append('They did well')
    return result