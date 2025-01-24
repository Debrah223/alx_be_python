class Calculator:
    """We include the class attribute"""
    calculation_type = "Arithmetic operations"

    @staticmethod
    def add(a, b):
        """We declare the static method to add to two numbers."""
        return a+b 
    
    @classmethod
    def multiply(cls, a, b):
        """We declare the class method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b 