
largest = -1000
smallest = 1000

number = int(input("Enter a number or 0 to cancel: "))
while number != 0:
    for i in range(number):
        if number > largest:
            print("The largest number is: ", number)
        else:
            print("The smallest number is: ", number)
    number = int(input("Enter a number or 1 to cancel: "))
