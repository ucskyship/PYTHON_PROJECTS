import string


def histogram(words: str) -> dict[str, int]:
    abc = string.ascii_lowercase

    map_ = {}

    for char in abc:
        map_[char] = words.lower().count(char)
    return map_


print(histogram("Alabama is a town"))
