def add(a, b):
    return a + b


addition = add

print(addition(1, 2))


print("-------------------------------------------------------------------------")


def operate(a, b, func):
    return func(a, b)


print(operate(1, 2, add))


print("-------------------------------------------------------------------------")


def func1():
    c = 4

    def func2():
        return c

    return func2()


print(func1())

print("-------------------------------------------------------------------------")


def plus(a):
    def func(b):
        return a + b
    return func


add_5 = plus(5)
print(add_5(10))

print("-------------------------------------------------------------------------")
