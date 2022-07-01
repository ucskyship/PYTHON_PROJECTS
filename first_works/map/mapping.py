list_of_numbers = [1, 2, 3, 4, 5]
mapped_list = list(map(lambda x: x**2, list_of_numbers))

# make a list in other to make it print more than once
# print(mapped_list) prints a mao object with reference to the address

print(mapped_list)
print(mapped_list)

#  print(list(mapped_list)) prints an empty list for efficiency’s sake. It loops though it once...

list_of_dict = [{"name": "Asake", "gender": "F"}, {"name": "Boyo", "gender": "M"}]
mapped_list_of_dict = list(map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict))

print(mapped_list_of_dict)
print([("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"] for x in list_of_dict])

filtered_list_of_dict = list(filter(lambda x: x["gender"] == "M", list_of_dict))
print(filtered_list_of_dict)