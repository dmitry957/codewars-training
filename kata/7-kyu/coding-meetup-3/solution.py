def is_ruby_coming(lst): 
    return any(dev for dev in lst if dev['language'] == 'Ruby')