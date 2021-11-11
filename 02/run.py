from parse import Parser
from time import process_time
from instance import Bag

from branchnbound import BranchAndBound
from fptas import FPTAS
from dp import DP
from redux import Redux
from greedy import Greedy


method = {
    'BNB':BranchAndBound,
    'DP':DP,
    'GRY':Greedy,
    'RDX':Redux,
    'FPTAS':FPTAS
}

def main():
    args = Parser().parse()
    res = args.file.replace('test', 'result').replace('inst', args.method)
    if args.method == 'FPTAS':
        res = res.replace('.dat', f'_{args.error}.dat')
    sol = args.file.replace('inst', 'sol')
    with open(args.file) as in_file, open(res, 'w') as res_file, open(sol) as sol_file:
        res_file.write('id,time_taken,sum_of_costs,optimal,best_solution\n')
        i = 0
        for line in in_file:
            instance = Bag.from_line(line)
            solver = method[args.method](instance)
            start = process_time()
            if args.method == 'FPTAS':
                solver.solve(error = args.error)
            else:
                solver.solve()
            end = process_time()
            stats = solver.stats()

            if args.method in ['BNB','GRY','RDX']:
                if args.method == 'BNB' and int(line.split()[1]) in [10, 15]: #20 22
                    start = process_time()
                    for j in range(10):
                        solver = method[args.method](instance)
                        solver.solve()
                        stats = solver.stats()
                    end = process_time()
                elif args.method == 'BNB' and int(line.split()[1]) in [20, 22, 25, 27, 30, 32, 35, 37, 40]: #25 27 30 32 35 37 40
                    solver = method[args.method](instance)
                    start = process_time()
                    solver.solve()
                    end = process_time()
                    stats = solver.stats()
                else: #4
                    start = process_time()
                    for j in range(1000):
                        solver = method[args.method](instance)
                        solver.solve()
                        stats = solver.stats()
                    end = process_time()



            sol_line = next(sol_file).split()
            while int(sol_line[0]) != instance.id:
                sol_line = next(sol_file).split()
            opt = int(sol_line[2])
            comb = [int(i) for i in sol_line[3:]]
            """
            if comb != stats['solution']:
                print(instance.capacity)
                print(stats['best_weight'])
                print(instance.items)
                print(comb)
                print(stats['solution'])
            """
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
            res_file.write(
                f'{instance.id},'
                f'{end-start},'
                f'{sum(cost for weight, cost in instance.items)},'
                f'{opt},'
                f'{stats["best_cost"]}\n'
            )
        print(i)



if __name__ == '__main__':
    main()
