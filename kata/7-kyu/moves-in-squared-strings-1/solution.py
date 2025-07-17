def vert_mirror(strng):
    substrs = strng.split('\n')
    return '\n'.join([s[::-1] for s in substrs])
    
def hor_mirror(strng):
    substrs = reversed(strng.split('\n'))
    return '\n'.join(substrs)
    
def oper(fct, s):
    return fct(s)