from copy import copy

class BranchAndBound:
    def __init__(self, instance):
        self.instance = instance
        self._stats = {
            'solved' : False,
            'configs_tried' : 0,
            'best_cost': 0,
            'best_weight': 0,
            'solution': [0 for i in range(len(instance.items))]

        }

    def solve(self):
        if self._stats['solved']:
            print('Already solved')
            return
        self._stats['solved'] = True
        rem_cost = sum(cost for weight, cost in self.instance.items)

        return self.__branchnbound(0, 0, 0, rem_cost, [0 for i in range(len(self.instance.items))])

    def stats(self):
        return self._stats

    def __branchnbound(self, item_id, current_weight, current_cost, remaining_cost, current_solution):
        self._stats['configs_tried'] += 1

        if current_weight > self.instance.capacity:
            return False

        if current_cost > self._stats['best_cost']:
            self._stats['best_cost'] = current_cost
            self._stats['best_weight'] = current_weight
            self._stats['solution'] = copy(current_solution)

        if current_cost + remaining_cost < self._stats['best_cost']:
            return False

        if item_id == len(self.instance.items):
            return False

        current_solution[item_id] = 1
        if self.__branchnbound(item_id + 1,
                            current_weight + self.instance.items[item_id][0],
                            current_cost + self.instance.items[item_id][1],
                            remaining_cost - self.instance.items[item_id][1],
                            current_solution):
            return True
        current_solution[item_id] = 0

        if self.__branchnbound(item_id + 1,
                            current_weight,
                            current_cost,
                            remaining_cost - self.instance.items[item_id][1],
                            current_solution):
            return True

        return False
