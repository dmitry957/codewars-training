def cut_fruits(fruits):
    result= []
    for fruit in fruits:
        if fruit in FRUIT_NAMES:
            mid = (len(fruit) + 1) // 2
            result.extend([fruit[:mid], fruit[mid:]])
        else:
            result.append(fruit)
    return result