from parse import Parser
from instance import Bag
from bruteforce import Bruteforce
from branchnbound import BranchAndBound


method = {
    'BF':Bruteforce,
    'BNB':BranchAndBound
}

def main():
    args = Parser().parse()
    sol = args.file.replace('inst', 'sol').replace('R', 'K')
    res = args.file.replace('tests', 'results')
    with open(args.file) as in_file, open(res, 'w') as res_file:
        for line in in_file:
            instance = Bag.from_line(line)
            solver = method[args.method](instance)
            solver.solve()
            stats = solver.stats()
            res_file.write(f'{instance.id} {stats["configs_tried"]}\n')


if __name__ == '__main__':
    main()
