def twoSum(list_of_numbers, target) -> list:
    for i in range(len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers) - 1):
            if list_of_numbers[i] + list_of_numbers[j] == target:
                return [i, j]

# this method is called O of n square time, this can be written as O(n^2), the states that this method will run in
# order of n times.


print(twoSum([3, 1, 5, -8], 8))


def two_sum(list_of_numbers: list, target: int) -> list:
    map_ = {}
    for i in range(len(list_of_numbers)):
        complement = target - list_of_numbers[i]

        if complement in map_:
            return [i, map_[complement]]
        else:
            map_[list_of_numbers[i]] = i

    return []


print(twoSum([3, 1, 5, -8], 8))

# this second method loops through the list just once and saves the first number it sees at its index in an empty
# dictionary with its element and : index, and then return the second complementary number that add for the sum when it
# sees it. This method helps us minimize time in trade for space. O for n.
