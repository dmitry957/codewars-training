from math import ceil
def pay_cheese(arr):
    total_wheels = sum(arr)
    total_minutes = total_wheels * 0.6
    total_hours = ceil(total_minutes / 60)
    total_wages = total_hours * 8.75 * 4
    return f'L{total_wages:.0f}'