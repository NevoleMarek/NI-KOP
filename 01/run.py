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
    with open(args.file) as file:
        for line in file:
            instance = Bag.from_line(line)
            #solver = method[args.method](instance)
            #solver.solve()

if __name__ == '__main__':
    main()
