class Redux:
    def __init__(self, instance):
        self.instance = instance
        self._stats = {
            'solved' : False,
            'best_cost': 0,
            'best_weight': 0,
            'solution': [0 for i in range(len(instance.items))]

        }

    def solve(self):
        if self._stats['solved']:
            print('Already solved')
            return
        orig_pos, sorted_items = zip(
                                *sorted(
                                    enumerate(self.instance.items),
                                    key=lambda x: x[1][0]/x[1][1]
                                    )
                                )
        self._stats['solved'] = True
        self.__redux(sorted_items, orig_pos)

        # Find the single best item to fit in bag and compare with greedy
        # heuristic result. Return the best ot the two.
        for item in sorted(self.instance.items, key=lambda x: x[1], reverse = True):
            if item[0] <= self.instance.capacity:
                if item[1] > self._stats['best_cost']:
                    self._stats['best_cost'] = item[1]
                    self._stats['best_weight'] = item[0]
                    self._stats['solution'] = [0 for i in range(len(self.instance.items))]
                    self._stats['solution'][self.instance.items.index(item)] = 1
                break


    def stats(self):
        return self._stats

    def __redux(self, sorted_items, orig_pos):
        weight, cost = 0, 0

        for item_id, item in enumerate(sorted_items):
            if weight + item[0] <= self.instance.capacity:
                self._stats['solution'][orig_pos[item_id]] = 1
                weight += item[0]
                cost += item[1]

        self._stats['best_cost'] = cost
        self._stats['best_weight'] = weight
