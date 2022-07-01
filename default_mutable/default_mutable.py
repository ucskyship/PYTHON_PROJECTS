############################################################
def appender(lst_=[]):
    lst_.append("You")
    return lst_


print(appender())
print(appender())
print(appender())
print(appender())


############################################################

def appender(lst=None):
    if lst is None:
        lst = []
    lst.append("You")
    return lst


print(appender())

print(appender())
print(appender())


###########################################################

def add(a: int = 0, b: int = 0) -> int:
    return a + b


print(add.__annotations__)


##########################################################

def sub(a: int = 0, b: int = 0) -> int:
    """Calculate the difference between two values"""
    return a + b


print(sub.__annotations__)
print(sub.__doc__)


##########################################################

def avg(*numbers):
    from statistics import mean
    return sum(numbers) / len(numbers)


print(avg(1, 3, 4, 5))


##########################################################

def avg(*numbers):
    from statistics import mean
    return mean(numbers)


print(avg(1, 3, 4, 5))
print(avg(1, 3, 4, 5))

lst__ = [1, 3, 4, 5]
set_ = {1, 3, 4, 5}

print(avg(*lst__, *set_))


#########################################################

def add(a=0, b=0, c=0):
    return a + b + c


d = dict(b=6, c=5, a=7)
print(d)
print(add(**d))


# we use double asteriks to park

#######################################################

def add(**kwargs):
    for k, v in kwargs.items():
        print(k, "==>", v)


add(b=6, c=5, a=7, g=7)


#######################################################

def add(a, *args, b=0, **kwargs):
    print()
    print(a, args, b, kwargs)
    print()
    print(a)
    print(args)
    print(b)
    print(kwargs)


add(5, 6, 7, 8, b=9, c=0, f=8, y=4)


def add(a, b, c, /, d):
    print(a, b, c, d)

    print(a, b, c, d)
    add(6, 9, 8)
