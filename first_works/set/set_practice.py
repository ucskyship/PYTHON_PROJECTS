s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {5, 7, 3}
s4 = {1, 2, 3, 4, 5, 6, 7, 9}

d1 = {'a': 1, 'b': 2, 'c': 4}


# #                                    SET

# #         DISJOINT
# # Because what is in s1 is also in s2, but will become true is what is in s1 is not in s2 Subset means what
# # is in s1 and also in s2, and the set which has more or extra elements becomes the super set of the the sub set
# # which has all common element
# print(s2.isdisjoint(s2))
# print(s1.issubset(s4))
# print(s1.issuperset(s2))
# print(s4.issuperset(s1))


# #       SYMMETRIC DIFFERENCE UPDATE
# # s1.symmetric_difference_update(s2)
# # print(s1)
# s1 ^= s2
# print(s1)


#       #       SYMMETRIC DIFFERENCE
# # it removes the intersection or what is common and then brings what is unique between the both of them
# s1 - s2 will give only what is in 1 and not in s2, but symmetric difference will give the difference of the both
# print(s1 ^ s2)
# print(s2 ^ s1)
# print(s1.symmetric_difference(s2))


#       DIFFERENCE UPDATE
# # all the things that are only in s1, that means anything in s1 and s2 will be removed, and it uses it to update s1
# note that it first finds the difference and then update
# s1.difference_update(s2)
# s1 -= s2
# print(s1)


#       DIFFERENCE
# # this means what is in s1 and not in s2
# s1 - s2
# print(s1)
# print(s2.difference(s1))


#       INTERSECTION UPDATE
# #  takes the intersection with what is in the both set and update it on s1. Example
# s1.intersection_update(s2)
# s1 &= s2
# print(s1)


#       INTERSECTION
# # intersection will tell what is common between the 2 sets and the symbol is ampersand '&'
# print(s1.intersection(s2))
# print(s1 & s2)


#       UPDATE
# s1 |= s2
# print(s1)
# s1.update(s2)
# print(s1)
# print(s1 | s2)
# print(s1.union(s2))


#       DISCARD and REMOVE
# 'discard' will discard the element you asked it to remove and throw an error message when it
# does not find what you asked it to remove 'remove' will remove the element and throw an error message when it
# doesn't find the element you asked it to remove s4.discard(10) s4.clear()


# print(s4)


# for i in s1:
#     print(i)
# s1.add(3)
# s1.add('r')
# s1.add('a')

# print(3, s1)
