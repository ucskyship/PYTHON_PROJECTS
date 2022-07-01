# assert (4 == 3, "4 must be equal to 3")


def tell_me_more_about(a_language: str) -> str:
    languages = ("Java", "Python", "Javascript")

    assert a_language in languages, f"language '{a_language}' not found"
    return a_language


print(tell_me_more_about("Java"))
print(tell_me_more_about("Haskell"))
