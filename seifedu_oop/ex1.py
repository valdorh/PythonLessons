class Point:
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print(f"Вызов __new__ для {cls} args: {args} ")
        return super().__new__(cls)

    def __init__(self, x, y):
        print(f"Вызов __инит__ для {self}")
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Удаление экземляра: {self}")

    def set_coords(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    pt = Point(2, 8)
    print(pt)