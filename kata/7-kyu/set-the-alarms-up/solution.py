from datetime import datetime, timedelta
def set_the_alarms_up(time, n):
    time_obj = datetime.strptime(time, '%H:%M')
    return [
        (time_obj + timedelta(minutes=5 * i)).strftime('%H:%M')
        for i in range(n)
    ]