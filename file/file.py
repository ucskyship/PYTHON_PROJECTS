# file = open("hello.txt", mode="w", encoding="utf-8")
#
# file.write("I love writing\n")
# file.write("I love reading\n")
# file.writelines(["I am prone to violence\n", "I am prone to violence\n"])
# file.close()

# or
#
# with open("hello.txt", mode="w", encoding="utf-8") as file:
#     file.write("I love writing\n")
#     file.write("I love reading\n")
#     file.writelines(["I am prone to violence\n", "I am prone to violence\n"])
# when you use the keyword with we no longer have to put the close file method, because python will open the file and
# close it.


# but when we change the mode="w" to mode="a" we will append to the file. Now the difference in the mode between "w"
# and "a" is that "write" overwrites that you've written before but "a" adds to the file.
# with open("hello.txt", mode="a", encoding="utf-8") as file:
#     file.write("\nI love writing\n")
#     file.write("I love reading\n")
#     file.writelines(["I am prone to violence\n", "I am prone to violence\n"])

# the "r" mode is for reading what is in the file.
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("I love writing\n")
    file.write("I love reading\n")
    file.writelines(["I am prone to violence\n", "I am prone to violence\n"])

# the "a" mode is for appending to the file.


# the keyword "r" helps to read what is in the text file
with open("hello.txt", mode="r", encoding="utf-8") as file:
    for index, line in enumerate(file.readlines()):
        print(f"line {index + 1}: {line}")
