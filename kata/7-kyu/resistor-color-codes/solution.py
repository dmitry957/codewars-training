def decode_resistor_colors(bands):
    color_codes = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange': '3',
        'yellow': '4',
        'green': '5',
        'blue': '6',
        'violet': '7',
        'gray': '8',
        'white': '9'
    }
    
    _bands = bands.split()
    ohms = int(''.join([color_codes.get(_bands[0], '0'), color_codes.get(_bands[1], '0')])) * 10**int(color_codes.get(_bands[2], '0'))
    tolerance = 5 if _bands[-1] == 'gold' else 10 if _bands[-1] == 'silver' else 20
    print(ohms)
    if ohms < 1000:
        return f'{ohms} ohms, {tolerance}%'
    elif ohms >= 10**3 and ohms < 10**6:
        result = f"{int(ohms/10**3)}k" if (ohms % 10**3 == 0) else f"{ohms/10**3:.1f}k" 
        return result + f" ohms, {tolerance}%"
    else:
        result = f"{int(ohms/10**6)}M" if (ohms % 10**6 == 0) else f"{ohms/10**6:.1f}M"
        return result + f" ohms, {tolerance}%"