__author__ = 'dias'


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.validate()

    def kind(self):
        longest = max(self.x, self.y, self.z)
        smallest = min(self.x, self.y, self.z)
        medium = self.x + self.y + self.z - longest - smallest

        if longest == smallest:
            return 'equilateral'

        if medium == smallest or medium == longest:
            return 'isosceles'

        return 'scalene'

    def validate(self):
        longest = max(self.x, self.y, self.z)
        smallest = min(self.x, self.y, self.z)
        medium = self.x + self.y + self.z - longest - smallest

        if longest <= 0 or smallest <= 0 or medium <= 0:
            raise TriangleError

        if longest >= medium + smallest:
            raise TriangleError


class TriangleError(Exception):
    pass


print(Triangle(4, 3, 4).kind())
