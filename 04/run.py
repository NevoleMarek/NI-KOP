from parse import Parser
import timeit
from instance import Bag
import json

from sa import SimulatedAnnealing


def main():
    args = Parser().parse()
    res = args.file.replace('test', 'result').replace('inst', f'sa_{args.alpha}_{args.temp_prob}')
    sol = args.file.replace('inst', 'sol')
    data = []
    with open(args.file) as in_file, open(sol) as sol_file, open(res, 'w') as res_file:
        res_file.write('id,time_taken,sum_of_costs,optimal,best_solution\n')

        i = 0
        for line in in_file:
            instance = Bag.from_line(line)
            solver = SimulatedAnnealing(instance, args.alpha, args.beta, args.temp_prob)
            start = timeit.default_timer()
            solver.solve()
            end = timeit.default_timer()


            sol_line = next(sol_file).split()
            while int(sol_line[0]) != instance.id:
                sol_line = next(sol_file).split()
            opt = int(sol_line[2])
            comb = [int(i) for i in sol_line[3:]]

            stats = solver.stats()
            stats['id'] = instance.id
            stats['time'] = end - start
            stats['optimal'] = opt
            data.append(stats)

            if opt != stats['best_cost']:
                i += 1
                """
                print(sol_line[0])
                print(opt)
                print(stats['best_cost'])
                print(instance.capacity)
                print(stats['best_weight'])
                print(comb)
                print(stats['solution'])
                """
            """

            """
            res_file.write(
                f'{instance.id},'
                f'{end-start},'
                f'{sum(cost for weight, cost in instance.items)},'
                f'{opt},'
                f'{stats["best_cost"]}\n'
            )
        print(i)

   # with open('result/n40.dat', 'w') as res_file:
    #    json.dump(data, res_file)




if __name__ == '__main__':
    main()
