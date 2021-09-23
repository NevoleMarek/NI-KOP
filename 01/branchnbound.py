class BranchAndBound:
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
        rem_cost = sum(cost for weight, cost in self.instance.items)
        return self.__branchnbound(0, 0, 0, rem_cost)

    def stats(self):
        return self._stats

    def __branchnbound(self, item_id, current_weight, current_price, remaining_cost):
        self._stats['configs_tried'] += 1

        if current_weight > self.instance.capacity:
            return False

        if current_price >= self.instance.min_price:
            return True

        if current_price + remaining_cost < self.instance.min_price:
            return False

        if item_id == len(self.instance.items):
            return False

        if self.__branchnbound(item_id + 1,
                            current_weight + self.instance.items[item_id][0],
                            current_price + self.instance.items[item_id][1],
                            remaining_cost - self.instance.items[item_id][1]):
            return True

        if self.__branchnbound(item_id + 1,
                            current_weight,
                            current_price,
                            remaining_cost - self.instance.items[item_id][1]):
            return True

        return False
