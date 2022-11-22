class Cat:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def __repr__(self):
        return f"{self.__class__} Name Cat: {self.name} {self.old} in old"


if __name__ == '__main__':
    cat = Cat("Vaska", 5)
    print(cat)