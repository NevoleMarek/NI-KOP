class Bag:
    def __init__(self):
        self.items = []
        self.capacity = 0
        self.id = 0

    @classmethod
    def from_line(cls, line):
        bag = cls()
        input_split = line.split()
        bag.id = int(input_split[0])
        bag.capacity = int(input_split[2])
        for i in range(int(input_split[1])):
            item = (int(input_split[2 * i + 3]), int(input_split[2* i + 4]))
            bag.items.append(item)
        return bag
