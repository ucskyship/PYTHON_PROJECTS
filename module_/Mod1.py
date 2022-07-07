print(__name__)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == '__main__':
    print("I am invisible to other modules")
    print("Mod1", __name__)
