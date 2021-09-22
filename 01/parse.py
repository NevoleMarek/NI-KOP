from argparse import ArgumentParser

class Parser:

    def __init__(self):
        self.parser = ArgumentParser(
                prog='Knapsack problem Solver',
                description=(
                    'Simple Knapsack problem Solver implementing Bruteforce'
                    ' solving method and Branch & Bound technique which'
                    ' improves on bruteforce algorithm.'))

    def parse(self):
        self.parser.add_argument(
            'file',
            type=str,
            help='path to file with tests')
        self.parser.add_argument(
            '--method',
            type=str,
            default='BF',
            help=(
                'Solver method: BF - bruteforce, BNB - Branch & BOund'
                ' Default is BF'))

        return self.parser.parse_args()
