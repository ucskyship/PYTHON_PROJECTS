def sum_num(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


"""Higher order function: is a function that takes other function as parameter, deal with it or can return other 
functions """

# def operate(fn, x, y):
#     fn(x, y)
#
#
# print(operate(lambda x, y: x * y, 3, 4))
#
# print(sum_num(3, 6))
#
#
# def subtract(a, b):
#     return a - b
#
#
# print(operate(sum_num, 2, 3))
# print(operate(subtract, 5, 2))

# print(sum_num.__name__)
# print(sum_num.__doc__)
# print(sum_num.__annotations__)
"""Regular function"""

# def add(x, y):
#     return x + y
#
#
# add = lambda x, y: x * y
#
# division = lambda p, q: p / q
# print(division(3, 5))
#
# print(division.__name__)


list_of_string = "I love Eden".split()

print(max(list_of_string, key=len))
print(max(list_of_string, key=lambda x: x[-1]))

ages = [{"name": "Adedayo", "age": 6}, {"name": "Titi", "age": 16}]

print(max(ages, key=lambda x: len(x["name"])))
print(max(ages, key=lambda x: x["age"]))
print(min(ages, key=lambda x: x["name"]))

print(sorted(ages, key=lambda x: len(x["name"])))
print(sorted(ages, key=lambda x: len(x["name"]), reverse=True))


