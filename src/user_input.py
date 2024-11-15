def input_prompt():
    # Get first operand from the user
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))
    return operator, operand1, operand2