"""The expression_parser module contains the logic for parsing a raw input expression
string from the user and turning it into an expression_list.

   Author: Kaylen Travis Pillay
   Date: 20 January 2019
   Location: Cape Town, South Africa
"""

from my_calculator.shunting_yard import is_number
from my_calculator.shunting_yard import is_operator

def parser(expression_string):
   """The parser function returns the expression tokens from the expression string
   in a list
   
   Arguments:
      expression_string {string} -- The raw input expression string
   """
   pointer_i = 0
   pointer_j = 0
   expression_list = []

   while pointer_j < len(expression_string):

      expression_token = expression_string[pointer_j]
      if is_number(expression_token):
         pointer_j += 1
         if pointer_j == len(expression_string):
            operand = expression_string[pointer_i : pointer_j]
            expression_list.append(operand)

      elif is_operator(expression_token):
         operand = expression_string[pointer_i : pointer_j]
         operator = expression_string[pointer_j]
         if not operand == '':
            expression_list.append(operand)
         expression_list.append(operator)
         pointer_j += 1
         pointer_i = pointer_j

      elif (expression_token == '(') or (expression_token == ')'):
         if not pointer_j == pointer_i:
            operand = expression_string[pointer_i : pointer_j]
            expression_list.append(operand)
         expression_list.append(expression_token)
         pointer_j += 1
         pointer_i = pointer_j

      else:
         if not pointer_j == pointer_i:
            operand = expression_string[pointer_i : pointer_j]
            expression_list.append(operand)
         pointer_j += 1
         pointer_i = pointer_j
   
   return expression_list


if __name__ == '__main__':
   list_ = parser("(4+8)*(6*5)  /  ( (3-2    )*     (   2      + 2)   )")
   print(list_)
