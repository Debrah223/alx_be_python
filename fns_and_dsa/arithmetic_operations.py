def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
    :param num1: First number (float)
    :param num2: Second number (float)
    :param operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')
    :return: Result of the operation or an error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
    