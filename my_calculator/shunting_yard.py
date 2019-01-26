"""The shunting-yard algorithm by Edsger W. Dijkstra, 
   (https://en.wikipedia.org/wiki/Edsger_W._Dijkstra),
   allows for the conversion of infix, i.e. (1 + 2) / 3, into RPN (Reverse
   Poilish Notation) or postfix notation, i.e. 1 2 + 3 /, which can be 
   easily evaluated by a computer through various algorithms.

   The basic concept of the shunting-yard algothim, SYA from here on, is
   the use of an operator ('+','-','*', etc.), stack for operators and 
   functions*, and an output queue. The SYA iterates over each expression
   token and check whether it is a number, function or operator and based 
   on the result peforms either a push onto the operator stack or a enque
   onto the output queue. The SYA is smart enough to maintain BODMAS rules
   of precendence when converting the infix expression into a postfix 'list'.
   This means that when the resulting postfix list is presented to the 
   postfix evaluation it automatically evaluates the expression with the 
   BODMAS rules (or any other customized rule set in the SYA) of precendence 
   intact. 

   For more information on the SYA see source below:
   Source (https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

   Author: Kaylen Travis Pillay
   Date: 20 January 2019
   Location: Cape Town, South Africa
"""
from re import compile

# Precedence dictionary
_PRECEDENCE_DICT = {'(':-1, ')':-1, '-':1, '+':2, '*':3, '/':4}
# Operator regular expression
_OPERATOR_REGEX = compile('[+-/*]')

def infix_to_postfix(expression_list):
    """The function uses the SYA to convert an infix expression list to
    a BODMAS sensitive expression list.
    
    Arguments:
        expression_list {list} -- This list contains expression tokens of type str
    """

    operator_stack = list()
    output_queue = list()

    for expression_token in expression_list:

        if is_number(expression_token):
            output_queue.append(expression_token)

        elif is_operator(expression_token):
            while check_precedence(expression_token, operator_stack):
                output_queue.append(operator_stack.pop())
            operator_stack.append(expression_token)

        elif is_left_bracket(expression_token):
            operator_stack.append(expression_token)

        elif is_right_bracket(expression_token):
            while not is_left_bracket(operator_stack[len(operator_stack) - 1]):
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue

def is_number(expression_token):
    """The is_number function tests whether an expression token is a number.
    
    Arguments:
        expression_token {string} -- An expression token to be evaluated.
    """
    try:
        float(expression_token)
        return True
    except Exception:
        return False

def is_operator(expression_token):
    """The is_operator function tests whether an expression token is an operator
    
    Arguments:
        expression_token {string} -- The expression token to be evaluated
    """
    if _OPERATOR_REGEX.match(expression_token):
        return True
    else:
        return False

def is_function(expression_token):
    """The is_function function tests whether an expression token is a function.
    
    Arguments:
        expression_token {string} -- The expression token to be evaluated
    """
    # TODO: Future implementation to allow for user functions in expression.
    pass

def is_left_bracket(expression_token):
    """The is_left_bracket function tests whether a expression token is a left bracket. '('
    NOTE: This function exists to allow better understanding of the SYA
    Arguments:
        expression_token {string} -- The expression token to be evaluated
    """
    return expression_token == '('

def is_right_bracket(expression_token):
    """The is_right_bracket function tests whether an expression token is a right bracket. ')'
    NOTE: This function exists to allow better understanding of the SYA.
    Arguments:
        expression_token {string} -- The expression token to be evaluated
    """
    return expression_token == ')'

def is_greater_or_equal_precedence(stack_operator, expression_token):
    """The is_greater_or_equal_precedence function tests whether the operator on 
    the top of the operator_stack has a greater than or equal precedence to the
    expression token.
    
    Arguments:
        stack_operator {string} -- The top operator from the operator_stack
        expression_token {string} -- The expression token to be evaluated
    """
    if _PRECEDENCE_DICT.get(expression_token) == None:
        return False
    
    elif stack_operator == None:
        return False

    elif _PRECEDENCE_DICT.get(stack_operator) == None:
        return False

    elif _PRECEDENCE_DICT.get(stack_operator) >= _PRECEDENCE_DICT.get(expression_token):
        return True
    
    else:
        return False

def check_precedence(expression_token, operator_stack):
    """The check_precedence function tests decides whether the expression token
    goes onto the output queue or not.
    NOTE: This function allows for a better understanding of the SYA
    Arguments:
        expression_token {string} -- The expression token to be evaluated
        operator_stack {list} -- The operator stack used in the SYA
    """
    if operator_stack:
        top_of_operator_stack = operator_stack[len(operator_stack) - 1]
    else:
        top_of_operator_stack = None
    return is_greater_or_equal_precedence(top_of_operator_stack, expression_token) or is_function(top_of_operator_stack) and not (is_left_bracket(top_of_operator_stack))


if __name__ == '__main__':
    expression_list = ['1', '+', '2', '-', '(', '2', '+', '9', ')']
    postfix_queue = infix_to_postfix(expression_list)

    # Expected result: [1, 2, +, 2, 9, +, -]
    print(postfix_queue)
