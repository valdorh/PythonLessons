class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def get_name(self):
        return self.__name

    def set_old(self, old):
        self.__old = old

    def set_name(self, name: str):
        self.__name = name

    old = property(get_old, set_old)
    name = property(get_name, set_name)


if __name__ == '__main__':
    p = Person("Vova", 60)
    p.old = 52
    p.name = "Olga"
    print(p.old, p.name, p.__dict__)
    for e in dir(p):
        print(e)

