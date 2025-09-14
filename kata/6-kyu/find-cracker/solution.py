def find_hack(arr):
    hacked = []
    def get_actual_score(grades):
        total = 0
        for grade in grades:
            match grade:
                case 'A': total += 30
                case 'B': total += 20
                case 'C': total += 10
                case 'D': total += 5
                case _: total += 0
        if len(grades) >= 5 and all(g in ('A', 'B') for g in grades):
            total += 20
        return min(total, 200)
    for item in arr:
        name, total, grades = item
        actual = get_actual_score(grades)
        if actual != total:
            hacked.append(name)
    return hacked