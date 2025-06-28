def zebulans_nightmare(function):
    parts = function.split('_')
    return parts[0] + ''.join([word.capitalize() for word in parts[1:]])