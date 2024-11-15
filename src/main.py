"""refactor: fonctions mathematiques deplacees dans math_functions.py """
"""refactor: fonctions prompt dans user_input.py """
from math_functions import add, subtract, multiply, divide
from user_input import input_prompt

def main(operator, operand1, operand2):

    # Perform the operation based on the operator
    if operator == '+':
        result = add(operand1, operand2)
    elif operator == '-':
        result = subtract(operand1, operand2)
    elif operator == '*':
        result = multiply(operand1, operand2)
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = divide(operand1, operand2)
    else:
        print("Invalid operator.")
        return

    # Print the result
    def display_result():
        print("Result:", operand1, operator, operand2, "=", result)

# Get inputs
operator, operand1, operand2 = input_prompt()

# Call the main function to run the program
main(operator, operand1, operand2)

display_result()
