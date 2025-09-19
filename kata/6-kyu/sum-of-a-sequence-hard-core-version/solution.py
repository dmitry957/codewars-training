def sequence_sum(begin_number, end_number, step):
    if step == 0:
        return 0
    
    if (begin_number > end_number and step > 0) or (begin_number < end_number and step < 0):
        return 0
    
    last_number = begin_number + ((end_number - begin_number) // step) * step
    n = ((last_number - begin_number) // step) + 1
    return n * (begin_number + last_number) // 2