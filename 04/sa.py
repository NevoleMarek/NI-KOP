import math
from random import choice, random
from copy import deepcopy

import numpy as np

def cooling_schedule(temp, alpha, beta = 0):
    return alpha * temp + beta

class SimulatedAnnealing:
    def __init__(self, instance, alpha, beta = 0, temp_prob = 0.8):
        self._instance = instance
        self._n = len(instance.items)
        self._alpha = alpha
        self._beta = beta
        self._temp_prob = temp_prob
        self._current_cost = 0
        self._current_weight = 0
        self._solved = False
        self._items = []
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
        self._items = [i for i, item in enumerate(self._instance.items) if item[0] <= self._instance.capacity]

    def _random_assignment(self):
        perm = np.random.permutation(np.array(self._items))
        weight = 0
        cost = 0
        items_in_bag = set()
        for i in perm:
            if self._instance.items[i][0] + weight > self._instance.capacity:
                continue

            weight += self._instance.items[i][0]
            cost += self._instance.items[i][1]
            items_in_bag.add(i)

        return items_in_bag, weight, cost

    def _initial_temperature(self):
        items = sorted(self._instance.items, key = lambda item: item[1], reverse = True)
        delta = items[0][1] - items[-1][1]
        temperature = abs(delta/math.log(self._temp_prob))
        return temperature


    def _random_item(self):
        """ Return id of random item"""
        return choice(self._items)

    def _next_solution(self, items_in_bag):
        new_items_in_bag = deepcopy(items_in_bag)
        new_weight = self._current_weight
        new_cost = self._current_cost

        item_to_add = None
        if len(self._items) != len(new_items_in_bag):
            item_to_add = self._random_item()
            while item_to_add in new_items_in_bag:
                item_to_add = self._random_item()

        if item_to_add is None: # All items are in bag
            return items_in_bag, new_weight, new_cost

        # Drop random items until items[item_id] can fit in the bag
        while (self._instance.items[item_to_add][0] + new_weight) > self._instance.capacity:

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
        items_in_bag, weight, cost = self._random_assignment()

        self._current_weight = weight
        self._current_cost = cost
        self._stats['cost_in_time'].append(self._current_cost)

        temperature = self._initial_temperature()

        self._stats['temperature_in_time'].append(temperature)

        best_cost = cost
        best_weight = weight
        best_bag = deepcopy(items_in_bag)

        iter_limit = len(self._instance.items) * 5
        iters = 0
        while iters < iter_limit:

            new_items_in_bag, new_weight, new_cost = self._next_solution(items_in_bag)
            delta = new_cost - self._current_cost
            if new_cost > self._current_cost:
                items_in_bag = new_items_in_bag
                self._current_weight = new_weight
                self._current_cost = new_cost
                iters = 0
            elif math.exp(delta/temperature) > random():
                items_in_bag = new_items_in_bag
                self._current_weight = new_weight
                self._current_cost = new_cost
                iters += 1
            else:
                iters += 1

            if best_cost < self._current_cost:
                best_cost = self._current_cost
                best_weight = self._current_weight
                best_bag = deepcopy(items_in_bag)

            temperature = cooling_schedule(temperature, self._alpha, self._beta)
            self._stats['temperature_in_time'].append(temperature)
            self._stats['cost_in_time'].append(self._current_cost)
            self._stats['iterations'] += 1
            #print(iters, items_in_bag, self._current_weight, self._current_cost, temperature)
        for i in best_bag:
            self._stats['solution'][i] = 1
        self._stats['best_cost'] = best_cost
        self._stats['best_weight'] = best_weight
