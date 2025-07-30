def missing(nums, s):
    s = s.replace(' ', '')
    result = []
    for index in sorted(nums):
        if 0 <= index < len(s):
            result.append(s[index].lower())
        else:
            return 'No mission today'
    return ''.join(result)