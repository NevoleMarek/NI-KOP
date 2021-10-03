from argparse import ArgumentParser

class Parser:

    def __init__(self):
        self.parser = ArgumentParser(
                prog='Knapsack problem Solver',
                description=(
                    'Knapsack problem Solver implementing backtrack solver'
                    ' improved by Branch&Bound method, solver using dynamic'
                    ' programming, bruteforce algorithm with greedy heuristics,'
                    ' REDUX (modifaction of greedy heuristics), FPTAS'
                    ' (modified DP technique).'))

    def parse(self):
        self.parser.add_argument(
            'file',
            type=str,
            help='path to file with tests')
        self.parser.add_argument(
            '--method',
            type=str,
            default='BNB',
            help=(
                'Solver method:'
                ' BNB - Branch & BOund,'
                ' DP - Dynamic programming,'
                ' GRY - Bruteforce greedy heuristics,'
                ' RDX - Redux greedy heuristics,'
                ' FPTAS - Fully polynomial-time approximation scheme using DP.'
                ' Default is BNB.'))
        self.parser.add_argument(
            '--error',
            type=float,
            default=1,
            help=(
                'Error parameter for FPTAS method.'
                ' Default is 1.'))

        return self.parser.parse_args()
