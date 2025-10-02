def is_centered(xs: list[int], n: int) -> bool:
    length = len(xs)
    if length == 0:
        return n == 0

    mid = length // 2
    center_sum = xs[mid] if length % 2 else 0
    left, right = mid - 1, mid + (1 if length % 2 else 0)

    while left >= 0 and right < length:
        if center_sum == n and left + 1 == length - right:
            return True
        center_sum += xs[left] + xs[right]
        left -= 1
        right += 1

    return center_sum == n and left + 1 == length - right