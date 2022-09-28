# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# human = Human("Ololade", 25, "F")
#
# print(human)

# ---------------------------------------------------

# from dataclasses import dataclass
#
#
#
#
# @dataclass
# class Human:
#     name: str
#     age: int = 0
#     gender: str = "F"
#
#
# human = Human("Ololade", 25, "F")
#
# print(human)

# ---------------------------------------------------

#
# from dataclasses import dataclass, field
#
#
# @dataclass(order=True, frozen=True)
# class Human:
#     name: str
#     age: int = field(default=0)
#     gender: str = field(default="F")
#     children: list[str] = field(default_factory=lambda: [], init=False, repr=False)
#
#
# human = Human("Ololade", 25, "F")
# alien = Human("Boyo", 45, "M")
#
# print(human < alien)
# print(human)
#
# # when you pass in a frozen=True parameter, the class is immutable that is it cannot change

# ---------------------------------------------------


from dataclasses import dataclass, field


@dataclass(order=True)
class Human:
    sort_by: tuple[int, str] = field(init=False, repr=False)
    name: str
    age: int = field(default=0)
    gender: str = field(default="F")
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)

    def __post_init__(self):
        self.sort_by = (self.age, self.name)


human = Human("Ololade", 25, "F")
alien = Human("Boyo", 45, "M")

human.name = "Dorcas"
print(human < alien)
print(human)
x = sorted([human, alien], key=lambda x: x.sort_by)
print(x)
