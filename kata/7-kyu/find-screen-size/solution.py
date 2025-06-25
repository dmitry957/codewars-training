def find_screen_height(width, ratio): 
    w, h = map(int, ratio.split(':'))
    return f"{width}x{h * width  // w}"