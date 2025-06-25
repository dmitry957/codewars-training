def reach_destination(distance, speed):
    time = round(distance / speed * 2) / 2
    return f"The train will be there in {int(time) if time == int(time) else '{0:.1f}'.format(time)} {'hour' if time == 1 else 'hours'}."
    