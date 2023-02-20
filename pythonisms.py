class Pythonisms:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item

    def __len__(self):
        return len(self)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value