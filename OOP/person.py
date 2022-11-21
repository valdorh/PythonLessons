class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError()
        self._age = age

    def describe(self):
        print(f" I am {self.first_name} {self.last_name}, Im {self._age} yars old!")