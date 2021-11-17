from parse import Parser
from timeit import default_timer
from instance import Bag

from branchnbound import BranchAndBound
from dp import DP
from greedy import Greedy


method = {
    'BNB':BranchAndBound,
    'DP':DP,
    'GRY':Greedy
}

def main():
    args = Parser().parse()
    res = args.file.replace('test', 'result').replace('inst', args.method)
    with open(args.file) as in_file, open(res, 'w') as res_file:
        res_file.write('id,time_taken,sum_of_costs,best_solution\n')
        for line in in_file:
            instance = Bag.from_line(line)
            solver = method[args.method](instance)
            start = default_timer()
            solver.solve()
            end = default_timer()
            stats = solver.stats()

            res_file.write(
                f'{instance.id},'
                f'{end-start},'
                f'{sum(cost for weight, cost in instance.items)},'
                f'{stats["best_cost"]}\n'
            )



if __name__ == '__main__':
    main()
