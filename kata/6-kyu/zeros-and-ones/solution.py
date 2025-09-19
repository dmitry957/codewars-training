def replace_zero(arr):
    max_length = 0
    zero_index = -1
    
    if 0 not in arr:
        return -1

    for i in range(len(arr)):
        if arr[i] == 0:
            left_count = 0
            for j in range(i - 1, -1, -1):
                if arr[j] == 1:
                    left_count += 1
                else:
                    break
            
            right_count = 0
            for j in range(i + 1, len(arr)):
                if arr[j] == 1:
                    right_count += 1
                else:
                    break
            
            current_length = left_count + right_count + 1
            if current_length >= max_length:
                max_length = current_length
                zero_index = i
                
    return zero_index