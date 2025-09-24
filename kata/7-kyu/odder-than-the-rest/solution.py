def odd_one(arr):
    return next((index for index, num in enumerate(arr) if num % 2 != 0), -1)