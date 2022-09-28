# class A:
#     def do_this(self):
#
#         print("from a")
#
#
# class C(A):
#     def do_this(self):
#         print("from c")
#
#
# class B(A):
#     def do_this(self):
#         print("from b")
#
#     class D(B, C):
#         def do_this(self):
#             print("from D")
#
#     help()


import abc


class Animal(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def name(self):
        return "Animal"

    @abc.abstractmethod
    def speak(self):
        return


class Dog(Animal):
    def speak(self):
        return super().name() + " -> " + "Dog"


def speak(self):
    return "gbo"


class Cat(Animal):

    def speak(self):
        return "meow"


dog = Dog()
cat = Cat()

print(dog.speak())
print(dog.name())
print(cat.speak())
