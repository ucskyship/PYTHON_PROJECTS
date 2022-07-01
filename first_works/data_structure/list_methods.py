# import random

rng = list(range(1, 100, 5))
print(rng)

# rng.append(1_000)
# print(rng)

# rng.append([2,3,4])
# print(rng)

# rng.extend([2,3,4])
# print(rng)

# rng += [2,3,4]
# print(rng)

# rng.insert(0, 55)
# print(rng)
#
# popped = rng.pop()
# print(rng)
# print(popped)

# rng.remove(41)
# print(rng)

# idx = rng.index(71)
# print(idx)
# print(rng)

# rng.clear()
# print(rng)

# lst = rng
# rng.clear()
# print(lst)
# print(rng)

# lst = rng
# rng.clear()
# print(id(lst))
# print(id(rng))

# lst = rng.copy()
# rng.clear()
# print(lst)
# print(rng)

# random.seed(45)
# random.shuffle(rng)
# print(rng)

# print(rng)
# print(random.choice(rng))

# rng.sort(reverse=True)
# print(rng)

# fruits = ["apple", "mango", "cherry", "banana", "cucumber", "pineapple"]
# fruits.sort()
# print(fruits)

# fruits = ["apple", "mango", "cherry", "banana", "cucumber", "pineapple"]
# fruits.sort(key=len)
# print(fruits)

fruits = ["apple", "mango", "cherry", "banana", "water melon", "cucumber", "pineapple", "orange"]
fruits.sort(key=len, reverse=True)
print(fruits)
