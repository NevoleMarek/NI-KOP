class Bruteforce:
    def __init__(self, instance):
        self.instance = instance
        self._stats = {
            'solved' : False,
            'configs_tried' : 1
        }

    def solve(self):
        if self._stats['solved']:
            print('Already solved')
            return
        self._stats['solved'] = True
        return self.__bruteforce(0, 0, 0)

    def stats(self):
        return self._stats

    def __bruteforce(self, item_id, current_weight, current_price):
        self._stats['configs_tried'] += 1

        if current_weight > self.instance.capacity:
            return False

        if current_price >= self.instance.min_price:
            return True

        if item_id == len(self.instance.items):
            return False

        # Add item_id into bag
        if self.__bruteforce(item_id + 1,
                            current_weight + self.instance.items[item_id][0],
                            current_price + self.instance.items[item_id][1]):
            return True

        # Do not add item_id into bag
        if self.__bruteforce(item_id + 1, current_weight, current_price):
            return True

        return False
