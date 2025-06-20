class MouseOver:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def find_rectangle(self, x, y):
        '''
        x0 ≤ x ≤ x0 + w
        y0 ≤ y ≤ y0 + h
        '''
        for rect in self.rectangles:
            x0, y0, width, height = rect
            if x0 <= x <= x0 + width and y0 <= y <= y0 + height:
                return rect
        return None