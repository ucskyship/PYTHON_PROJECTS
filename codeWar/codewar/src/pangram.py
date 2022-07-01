import string


# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())


# print(is_pangram("The fox jumps over the lazy dog"))


#  or

def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.ascii_lowercase)


print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("The fox jumps over the dog"))
