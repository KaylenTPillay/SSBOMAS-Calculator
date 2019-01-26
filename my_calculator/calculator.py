from my_calculator.shunting_yard import infix_to_postfix
from my_calculator.shunting_yard import is_number
from my_calculator.shunting_yard import is_operator
from my_calculator.expression_parser import parser

class calculator:
    def __init__(self):
        self.operation_lookup = {'+':self.add, '-':self.subtract, '/':self.divide, '*':self.multiply}

    def parse(self, expression_string):
        """The parse function gets the expression string ready to be evaluated
        
        Arguments:
            expression_string {string} -- The raw expression input string
        """
        expression_list = parser(expression_string)
        expression_queue = infix_to_postfix(expression_list)
        return expression_queue

    def execute(self, expression_string):
        """Executes the raw input expression string
        
        Arguments:
            expression_string {string} -- The raw expression input string
        """
        expression_list = self.parse(expression_string)
        operand_stack = list()

        for expression_token in expression_list:
            if is_number(expression_token):
                operand_stack.append(expression_token)

            elif is_operator(expression_token):
                operand_2 = float(operand_stack.pop())
                operand_1 = float(operand_stack.pop())
                operator = self.operation_lookup.get(expression_token)
                result = operator(operand_1, operand_2)
                operand_stack.append(str(result))

        if operand_stack:
            return operand_stack.pop()
        else:
            return None

    @staticmethod
    def add(operand_1, operand_2):
        return operand_1 + operand_2

    @staticmethod
    def subtract(operand_1, operand_2):
        return operand_1 - operand_2

    @staticmethod
    def divide(operand_1, operand_2):
        if not operand_2 == 0:
            return operand_1 / operand_2
        else:
            return ValueError("Division by Zero")

    @staticmethod
    def multiply(operand_1, operand_2):
        return operand_1 * operand_2


if __name__ == '__main__':
    cal = calculator()
    answer = cal.execute('(300+23)*(43-21)/(84+7)')
    print(answer)
