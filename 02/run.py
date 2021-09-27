from parse import Parser
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
    res = args.file.replace('tests', 'results').replace('inst', args.method)
    sol = args.file.replace('inst', 'sol')
    with open(args.file) as in_file, open(res, 'w') as res_file, open(sol) as sol_file:
        res_file.write('id,tries\n')
        for line in in_file:
            instance = Bag.from_line(line)
            solver = method[args.method](instance)
            solver.solve()
            stats = solver.stats()
            sol_line = next(sol_file).split()
            opt = int(sol_line[2])
            #comb = [int(i) for i in sol_line[3:]]
            if opt != stats['best_cost']:
                print(line)
            res_file.write(f'{instance.id},{stats["configs_tried"]}\n')



if __name__ == '__main__':
    main()
