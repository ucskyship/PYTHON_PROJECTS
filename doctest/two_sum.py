def twoSum(list_of_numbers, target):

    for i in range(len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers) - 1):
            if list_of_numbers[i] + list_of_numbers[j] == target:
                return [i, j]


print(twoSum([3, 1, 5, -8], 8))
