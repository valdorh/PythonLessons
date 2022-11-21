from cat import Cat
from person import Person

if __name__ == '__main__':
    tom = Cat("Tom", 3)
    angela = Cat("Angela", 9)
    print(tom, "TOM")
    print(angela, "ANGELA")
    angela.meow()
    tom.meow()
    print(tom.meow())
    print('=' * 25)
    # -----------------------Person-----------------------------
    ivan = Person("Vladimir", "Doronin", 60)

    ivan.describe()
