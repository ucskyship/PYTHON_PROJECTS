class Person:
    # __slots__ = ('name', 'age')

    # const __new__(cls, *args, **kwargs):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Iam {self.name} and {self.age} yrs old"

    def __repr__(self):
        return f"Person ({self.name}, {self.age})"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __format__(self, format_spec):
        if format_spec == 'n':
            return self.name
        else:
            return str(self)

    def __len__(self):
        return len(self.name)


omotee = Person(name="Omotola", age=20)
shafspec = Person(name="Abdur-Rahman", age=25)

print(f"{omotee!s}")
print(omotee == shafspec)
print(omotee < shafspec)

omotee.name = "Wire"
print(omotee.name)
print(omotee.__dict__)

# when we define a slot we limit the dict saying these are the only attribute it is supposed to have
