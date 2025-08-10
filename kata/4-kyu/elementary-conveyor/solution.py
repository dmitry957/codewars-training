from collections import deque

def path_counter(m):
    rows = len(m)
    cols = len(m[0])
    f_pos = None
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == 'f':
                f_pos = (row, col)
                break
        if f_pos:
            break
    
    directions_map = {
        'r': (0, 1),
        'l': (0, -1),
        'u': (-1, 0),
        'd': (1, 0),
        'f': (0, 0)
    }
    
    reverse_graph = [[[] for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            d = m[row][col]
            if d == 'f':
                continue
            dr, dc = directions_map[d]
            nr = (row + dr) % rows
            nc = (col + dc) % cols
            reverse_graph[nr][nc].append((row, col))
    
    dist = [[-1] * cols for _ in range(rows)]
    dist[f_pos[0]][f_pos[1]] = 0
    
    q = deque([f_pos])
    while q:
        r, c = q.popleft()
        for rr, cc in reverse_graph[r][c]:
            if dist[rr][cc] == -1:
                dist[rr][cc] = dist[r][c] + 1
                q.append((rr, cc))
                
    return dist