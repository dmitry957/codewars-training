def remove_duplicate_ids(obj):
    result = {}
    char_to_key = {}
    sorted_keys = sorted(obj.keys(), key=lambda k: int(k), reverse=True)

    for key in sorted_keys:
        for char in obj[key]:
            if char not in char_to_key:
                char_to_key[char] = key

    for key in obj.keys():
        new_array = []
        for char in obj[key]:
            if char_to_key.get(char) == key and char not in new_array:
                new_array.append(char)
        result[key] = new_array

    return result