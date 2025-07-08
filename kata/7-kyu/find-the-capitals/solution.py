def capital(capitals): 
    result = []
    for item in capitals:
        sentence = f"The capital of {item['state'] if 'state' in item else item['country']} is {item['capital']}"
        result.append(sentence)
    return result