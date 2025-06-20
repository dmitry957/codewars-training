from collections import defaultdict

class MouseOver:
    def __init__(self, rectangles):
        self.rectangles = rectangles
        self.grid_size = 3000
        self.grid = defaultdict(list)

        for index, (x, y, width, height) in enumerate(rectangles):
            x1, x2 = x, x + width
            y1, y2 = y, y + height
            gx1, gx2 = x1 // self.grid_size, x2 // self.grid_size
            gy1, gy2 = y1 // self.grid_size, y2 // self.grid_size
            for gx in range(gx1, gx2 + 1):
                for gy in range(gy1, gy2 + 1):
                    self.grid[(gx, gy)].append(index)
        
    def find_rectangle(self, x, y):
        gx, gy = x // self.grid_size, y // self.grid_size
        for index in self.grid.get((gx, gy), []):
            x0, y0, width, height = self.rectangles[index]
            if x0 <= x <= x0 + width and y0 <= y <= y0 + height:
                return (x0, y0, width, height)
        return None
