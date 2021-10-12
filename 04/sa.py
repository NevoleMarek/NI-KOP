import math
from random import choice
from copy import deepcopy

import numpy as np
from numpy import random

def cooling_schedule(temp, alpha, beta = 0):
    return alpha * temp + beta


class SimulatedAnnealing:
    def __init__(self, instance, alpha, beta = 0):
        self._instance = instance
        self._n = len(instance.items)
        self._alpha = alpha
        self._beta = beta
        self._current_cost = 0
        self._current_weight = 0
        self._solved = False
        self._stats = {
            'cost_in_time': [],
            'temperature_in_time': [],
            'iterations': 0,
            'best_weight': 0,
            'best_cost': 0,
            'solution': [ 0 for i in range(len(instance.items))]
        }

    def stats(self):
        return self._stats

    def _discard_useless_items(self):
        self._instance.items = [item for item in self._instance.items if item[0] < self._instance.capacity]


    def _random_assignment(self):
        perm = random.permutation(np.array([i for i in range(len(self._instance.items))]))
        weight = 0
        cost = 0
        items_in_bag = {}
        for i in perm:
            if self.instance.items[i][0] + weight > self.instance.capacity:
                break

            weight += self.instance.items[i][0]
            cost += self.instance.items[i][1]
            items_in_bag.add(i)

        return items_in_bag, weight, cost

    def _initial_temperature(self, items_in_bag):
        pass

    def _random_item(self):
        """ Return id of random item"""
        return choice(range(len(self._instance.items)))

    def _next_solution(self, items_in_bag):
        new_items_in_bag = deepcopy(items_in_bag)
        new_weight = self._current_weight
        new_cost = self._current_cost

        item_to_add = None
        if len(self._instance.items) != len(new_items_in_bag):
            item_to_add = self._random_item()
            while item_to_add in new_items_in_bag:
                item_to_add = self._random_item()

        if item_to_add is None: # All items are in bag
            return items_in_bag, new_weight, new_cost

        # Drop random items until items[item_id] can fit in the bag
        while (self._instance.items[item_to_add][0] + self._current_weight) > self._instance.capacity:

            item_to_remove = self._random_item()
            while item_to_remove not in new_items_in_bag:
                item_to_remove = self._random_item()

            new_weight -= self._instance.items[item_to_remove][0]
            new_cost -= self._instance.items[item_to_remove][1]
            new_items_in_bag.remove(item_to_remove)

        new_weight += self._instance.items[item_to_add][0]
        new_cost += self._instance.items[item_to_add][1]
        new_items_in_bag.add(item_to_add)

        return new_items_in_bag, new_weight, new_cost



    def solve(self):
        if self._solved:
            raise Exception(message='Already solved.')
        self._solved = True

        self._discard_useless_items()

        items_in_bag= self._random_assignment()

        self._current_weight = weight
        self._current_cost = cost
        self._stats['cost_in_time'].append(cost)

        temperature = self._initial_temperature(items_in_bag)

        self._stats['temperature_in_time'].append(temperature)

        iter_limit = len(self.instance.items) * 20
        iters = 0
        while iters < iter_limit:

            new_items_in_bag, new_weight, new_cost = self._next_solution(items_in_bag)
            delta = new_cost - self._current_cost
            if new_cost > self._current_cost or math.exp(delta/temperature) > random.random(0,1):
                items_in_bag = new_items_in_bag
                weight = new_weight
                cost = new_cost
                iters = 0
            else:
                iters += 1

            temperature = cooling_schedule(temperature, self._alpha, self._beta)
            self._stats['temperature_in_time'].append(temperature)
            self._stats['cost_in_time'].append(cost)
