class Counter:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration


# count = Counter(1, 10)
for count in Counter(1, 10):
    print(count)