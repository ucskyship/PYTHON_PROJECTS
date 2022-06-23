for num in range(1, 101, 1):

    if num % 15 == 0:
        print("FIZZBUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    elif not num % 5:
        print("BUZZ")
    else:
        print(num)
