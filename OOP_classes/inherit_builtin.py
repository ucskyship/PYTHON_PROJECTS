from enum import Enum, auto, unique, Flag


@unique
# class AgeGroup(Enum):
class AgeGroup(Flag):
    # KID = auto()
    KID = 1
    ADOLESCENT = 32
    ADULT = 128


kids = AgeGroup.KID | AgeGroup.ADOLESCENT

print(kids)
# print(AgeGroup.KID.name)
# print(AgeGroup.KID.value)
