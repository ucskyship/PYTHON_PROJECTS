import string


def histogram(words: str) -> dict[str, int]:
    return {char: words.lower().count(char) for char in string.ascii_lowercase}


print(histogram("Hey hello how are you doing to day and i hope your are doing okay"))

#     abc = string.ascii_lowercase
#
#     map_ = {}
#
#     for char in abc:
#         map_[char] = words.lower().count(char)
#     return map_
#
#
# print(histogram("Alabama is a town"))
