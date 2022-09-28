# from typing import Self


class Person:
    number_of_persons = 0

    def __init__(self, name: str, age=17) -> None:
        self.name = name
        self._age = age
        Person.number_of_persons += 1

    @classmethod
    def get_number_of_persons(cls):
        return cls.number_of_persons

    @staticmethod
    def determine_class(age: int) -> str:
        if age >= 18:
            return "Major"
        return "Minor"

    @property
    def name(self):
        print("You're calling me")
        return self._name

    @name.setter
    def name(self, name):
        print("Setter")
        if "f" in name:
            print("Fuck off")
            return
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise "age cannot be less than 0"
        self._age = new_age

    #     decorated methods,
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        print("name will now be deleted")
        del self._name


person1 = Person("Abigail")
person1.name = "Omotee A1"
person12 = Person("Dorcas", 56)
print(dir(person1))

print(person1.name)
print(Person.determine_class(34))
