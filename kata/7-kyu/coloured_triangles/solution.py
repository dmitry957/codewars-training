def triangle(row):
    if len(set(row)) == 1:
        return row[0]
            
    def next_color(c1, c2):
        if c1 == c2:
            return c1
        colors = { 'R', 'G', 'B' }
        return (colors - {c1, c2}).pop()
    
    next_row = ''.join(next_color(row[i], row[i+1]) for i in range(len(row)-1))
    return triangle(next_row)