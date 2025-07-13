def encode(s:str) -> str:
    return circle_cipher(s, False)
    
    
def decode(s:str) -> str:
    return circle_cipher(s, True)
    
def circle_cipher(s:str, is_decode:bool) -> str:
    result = [''] * len(s)
    left, right = 0, len(s) - 1
    index = 0
    while left <= right:
        if not is_decode:
            result[index] = s[left]
            if index + 1 < len(s):
                result[index + 1] = s[right]
        else:
            result[left] = s[index]
            if index + 1 < len(s):
                result[right] = s[index + 1]
        index += 2
        left += 1
        right -= 1
    return ''.join(result)