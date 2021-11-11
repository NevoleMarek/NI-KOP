from argparse import ArgumentParser

class Parser:

    def __init__(self):
        self.parser = ArgumentParser(
                prog='Knapsack problem Solver',
                description=(
                    'Knapsack problem Solver implementing metaheuristic of '
                    'simulated annealing.'))

    def parse(self):
        self.parser.add_argument(
            'file',
            type=str,
            help='path to file with tests')
        self.parser.add_argument(
            '--alpha',
            type=float,
            default=0.99,
            help=(
                'Alpha parameter for cooling schedule.'
                ' Default is 0.99'))
        self.parser.add_argument(
            '--beta',
            type=float,
            default=0,
            help=(
                'Beta parameter for cooling schedule.'
                ' Default is 0'))
        self.parser.add_argument(
            '--temp_prob',
            type=float,
            default=0.8,
            help=(
                'Parameter used in computation of initial temperature.'
                ' Determines with what probability the move, where best item'
                ' (in terms of price) '
                ' is replaced with the worst item, is accepted.'
                ' Default is 0.8'))

        return self.parser.parse_args()
