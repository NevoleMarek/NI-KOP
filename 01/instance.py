class Bag:
    def __init__(self):
        self.items = []
        self.capacity = 0
        self.id = 0
        self.min_price = 0

    @classmethod
    def from_line(cls, line):
        bag = cls()
        input_split = line.split()
        bag.id = input_split[0]
        bag.capacity = int(input_split[2])
        bag.min_price = int(input_split[3])
        for i in range(len(input_split[4:])//2):
            item = (int(input_split[2 * i + 4]), int(input_split[2* i + 5]))
            bag.items.append(item)
        return bag
