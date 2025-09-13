def time_stamp(times):
    year, month, day, hour, minute, second = times
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    days = 0
    for y in range(1970, year):
        days += 366 if is_leap(y) else 365
    for m in range(1, month):
        if m == 2 and is_leap(year):
            days += 29
        else:
            days += month_days[m - 1]
    days += day - 1
    seconds = days * 86400 + hour * 3600 + minute * 60 + second
    return seconds