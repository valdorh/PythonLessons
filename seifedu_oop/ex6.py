class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Не тот тип аргумента")

    def get_coord(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(5, 9)
    print(pt.get_coord())
    pt.set_coord(12, 19)
    print(pt.get_coord())
