class Cat:
    _lcvar = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} Say: Meow!, Meow!, Meow!")

