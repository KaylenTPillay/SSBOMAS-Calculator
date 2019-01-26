from argparse import ArgumentParser
from my_calculator.calculator import calculator

def main():
    parser = ArgumentParser(description='This tool evalutates an expression')
    parser.add_argument('expression_string', metavar='expression', type=str, help='Expression string for evaluation.')
    args = parser.parse_args()
    cal = calculator()
    return cal.execute(args.expression_string)