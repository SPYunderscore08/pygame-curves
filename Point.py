class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y

    def add(self, point):
        self.x += point.x
        self.y += point.y
        return self

    def subtract(self, point, copy=False):
        if copy:
            return Point(
                self.x - point.x,
                self.y - point.y
            )
        self.x -= point.x
        self.y -= point.y
        return self

    def multiply(self, point):
        self.x *= point.x
        self.y *= point.y
        return self

    def divide(self, point):
        self.x = self.x / point.x
        self.y = self.y / point.y
        return self

    @staticmethod
    def calculate_midpoint(start_point, end_point):
        return end_point.subtract(start_point, True).divide(2, 2)

    def __copy__(self):
        return Point(
            self.x,
            self.y
        )
