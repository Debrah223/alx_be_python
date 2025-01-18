# robust_division_calculator

def safe_divide(numerator, denominator):
    """We are going to perform division with error handling.
    Args:
        numerator (any): The numerator for the division.
        denominator (any): The denominator for the division.
        
        Returns:
            str: Result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        #Attempt division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
