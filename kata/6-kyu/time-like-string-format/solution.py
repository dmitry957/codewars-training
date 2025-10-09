def solution(hour): 
    hour = str(hour)
    if len(hour) < 3 or len(hour) > 4:
        raise ValueError('Hour length must be between 3 and 4 digits.')
    return f'{hour[:-2]}:{hour[-2:]}'