class Dog:
    pass


class Dog:
    species = "Canis familiaries"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} year old"

    def speak(self, sound):
        return f"{self.name} miles{sound} sound"

    miles = Dog("Miles", 4)
    miles.__str__()

    miles.speak = Dog("Woof woof")
    miles.speak()

    names = ["Ace", "Bace", "Lace"]
    print(names)

