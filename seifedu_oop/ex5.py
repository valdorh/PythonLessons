class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y ):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return {self.x, self.y}

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


if __name__ == '__main__':
    v = Vector(2, 200)
    print(Vector.norm2(5, 6))
    print(v.norm2(5, 6))
    print(v.get_coord())