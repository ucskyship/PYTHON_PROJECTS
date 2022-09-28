# def generate():
#     start = 1
#     while True:
#         yield start
#         start += 1
# print("-------------------------------------------------------------------------")

#
# gen = generate()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print("-------------------------------------------------------------------------")


# def generate(num):
#     start = 1
#     while start <= num:
#         yield start
#         start += 1
#         yield "poof"
#
#
# gen = generate(num=10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# print(list(gen))
# print("-------------------------------------------------------------------------")

def generate(num):
    start = 1
    while start <= num:
        yield start
        start += 1
        yield "poof"


gen = generate(num=10)

gen_exp = (num for num in range(1, 11))

print("Gen exp", gen_exp)

print(next(gen))
print(next(gen))
print(next(gen))

print(list(gen))
