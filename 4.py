class NumberGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
generator = NumberGenerator(1, 5)
for num in generator:
    print(num)