s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {5, 7, 3}
s4 = {1, 2, 3, 4, 5, 6, 7, 9}

d1 = {'a': 1, 'b': 2, 'c': 4}

# #                                      DICTIONARY
# d = dict(a=1, b=2, c=3)
#
# #  to add value of range to a dictionary
# print({}.fromkeys('abcde', list(range(5))))
#
# #  to add to a dictionary a key and a vlue that does not exist
# d.setdefault('d', 8)
# print(d)

# #  takes key and value, which means 'a' is the key and 1 os the value
# #  lets you pop with the key and not with the value and when it doesn't find it, it throws and error message
# # remember pop allows you remove at random
# d1.popitem()
# d1.clear()

#       UPDATE
# #  updates the value of the key but does not update the key, and what ever key and value isn't there will be added
# d1.update({'a': 5, 'g': 10})
# # print(d1)
# # print(d1.items())
# # print(list(d1.items()))
# # print(list(d1.values()))
# print(d1.keys())
# print(d1)

# #     LOOP
# whenever you are looping ta dictionary what it gives is the key and the value because the key is what is
# # holding the values
# #  but in other to get the value of the key see next method
# #  to loop through the values of a dictionary

# # for key in d1.keys():
# #     print(key)

#      or

# for key in d1:
#     print(d1[key])

#      or

# # for k in d1.values():
# #     print(k)

#       or

# for key, value in d1.items():
#     print(f"{key} -> {value}")

# #       RAW
# print(r"I \n love \n it \n raw")

# #         TO GET VALUE WITHOUT ERROR or TO GET REPLACE A NON-FOUND KEY WITH A VALUE
# # print(d1.get('t', 8))
# # print(d1.get('a'))
# print(d1.get('r', "UNKNOWN KEY"))
#
#
