def rotate(lst, k):
    k = k % len(lst)

    lst_a = lst[k:]
    lst_b = lst[:k]

    return lst_a + lst_b


list_to_rotate = rotate([7, -3, 2, 4, 9], 3)
print("This the rotated result of  {} times is: {}.".format(3, list_to_rotate))
