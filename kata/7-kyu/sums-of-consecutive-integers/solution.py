def position(x,y,n):
    a = (y - (x * (x - 1) // 2)) // x
    return a + n