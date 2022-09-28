# lst = [1, 2, 3, 4]
#
# try:
#     s = lst[9]
#     d = 4 + "I "
#     print("I did well")
# except IndexError as e:
#     print(f"Error occurred: {e}")
#
# except TypeError as e:
#     print(f"Error occurred: {e}")
#
# finally:
#     print("I am finally done")


# when you're inside the try and any error occur the except block will be executed. when you're inside the try and no
# error occur the except block will not be executed. you can catch any exception by using just the except keyword.
# you can catch multiple exceptions from line 9 when multiple error occurs, the catch for the first error will be
# executed before that of the second catches. you can catch multiple exceptions from line 9 with a tuple. finally
# block is always executed if or no error. if then's an error occur, except runs, else runs and then finally. if the
# loop terminates by itself the else runs. else will only occur if no error occurs in the try block. if they "is" a
# try block, they must be an except block and or an else block, but if you don't have an except block nor an else
# block, you must have a "finally block".


def square(s: int | float) -> int | float:
    if isinstance(s, int):  # this is to get the type of what is passed into function
        return s * s
    raise ValueError("I can only square an integer or a float")


try:
    print(square([7]))
except IndexError as e:
    print(f"Error occurred: {e}")

except (TypeError, ValueError) as e:
    print(f"Error occurred: {e}")


finally:
    print("I am finally done")
