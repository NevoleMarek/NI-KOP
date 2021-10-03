import numpy as np
from copy import deepcopy

MAXINT = 922337203685477580

class FPTAS:
    def __init__(self, instance):
        self.instance = instance
        self._stats = {
            'solved' : False,
            'best_cost': 0,
            'best_weight': 0,
            'solution': [0 for i in range(len(instance.items))]

        }

    def solve(self, error):
        if self._stats['solved']:
            print('Already solved')
            return
        self._stats['solved'] = True

        # Find item with highest price that can fit in the bag
        for weight, cost in sorted(self.instance.items, key = lambda x: x[1], reverse=True):
            max_cost = cost
            if weight < self.instance.capacity:
                break

        # Modify price of each item to cost categories according to set error
        K = (error * max(self.instance.items, key = lambda x: x[1])[1]) / len(self.instance.items)
        items = [(weight, int(cost//K)) for weight, cost in self.instance.items]
        best_possible_cost = sum(cost for weight, cost in items)

        # Instantiate memory table for dynamic programming
        self._dp = np.full((best_possible_cost + 1, len(self.instance.items) + 1), MAXINT)
        self._dp[0, 0] = 0

        self.__solve(best_possible_cost, items)

        # Compute cost according to solution
        cost = 0
        for i, item in enumerate(self.instance.items):
            if self._stats['solution'][i] == 1:
                cost += item[1]
        self._stats['best_cost'] = cost

    def stats(self):
        return self._stats

    def __solve(self, best_possible_cost, items):
        for i in range(1,self._dp.shape[1]):
            for c in range(self._dp.shape[0]):
                if c - items[i-1][1] < 0:
                    self._dp[c, i] = self._dp[c, i-1]
                    continue

                self._dp[c][i] = min(
                    [
                        self._dp[c, i-1],
                        self._dp[c - items[i-1][1], i-1] + items[i-1][0]
                    ]
                )

        for i in range(self._dp.shape[0]- 1 ,0,-1):
            if self._dp[i, self._dp.shape[1] - 1] <= self.instance.capacity:
                self._stats['best_cost'] = i
                self._stats['best_weight'] = self._dp[i][self._dp.shape[1] - 1]
                break

        cost = self._stats['best_cost']
        i = len(items)
        while cost != 0:
            for j in range(i):

                if self._dp[cost, i - (j + 1)] != self._dp[cost, i - j]:
                    cost -= items[(i - 1) - j][1]
                    self._stats['solution'][(i - 1) - j] = 1
                    i -= j
                    break
