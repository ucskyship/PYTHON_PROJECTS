class MyCustomList(list):

    # def __init__(self):
    #     self.my_list = []

    def __getitem__(self, item):
        print("getting my item")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if value < 1:
            print("Not adding it")
            return
        super().__setitem__(key, value)

    def append(self, item) -> None:
        if item < 1:
            return
        super().append(item)


c = MyCustomList()
print(c)
c.append(9)
c.append(-1)
# c[1] = -6
print(c)

# -----------------------------------------------------------------------------------------------


class MyDictionary(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_dict = {}

    def save(self, key, value):
        self.my_dict[key] = value
        print(self.my_dict)

    def my_dict(self):
        with open("my_dict.txt", "w") as f:
            for key, value in self.my_dict.items():
                f.write(f"{key} : {value}\n")


