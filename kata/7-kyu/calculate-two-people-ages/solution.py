def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return None
    older_age = (sum_ + difference) / 2
    younger_age = sum_ - older_age
    if older_age < 0 or younger_age < 0:
        return None
    return (older_age, younger_age)