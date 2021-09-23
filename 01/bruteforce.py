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
        if current_weight > self.instance.capacity:
            return False

        if current_price >= self.instance.min_price:
            return True

        if item_id == len(self.instance.items):
            return False

        for truth_value in [1,0]:

            if truth_value:
                self._stats['configs_tried'] += 1
                current_weight += self.instance.items[item_id][0]
                current_price += self.instance.items[item_id][1]

            if self.__bruteforce(item_id + 1, current_weight, current_price):
                return True

            if truth_value:
                current_weight -= self.instance.items[item_id][0]
                current_price -= self.instance.items[item_id][1]
        return False
