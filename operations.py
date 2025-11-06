"""
Calculator operations module
Contains all arithmetic calculation functions
"""


class DivisionByZeroError(Exception):
    """Custom exception for division by zero"""
    pass


class InvalidOperationError(Exception):
    """Custom exception for invalid operations"""
    pass


def add(num1: float, num2: float) -> float:
    """
    Add two numbers
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Sum of num1 and num2
    """
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    """
    Subtract second number from first number
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Difference of num1 and num2
    """
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """
    Multiply two numbers
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        Product of num1 and num2
    """
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    """
    Divide first number by second number
    
    Args:
        num1: Numerator
        num2: Denominator
        
    Returns:
        Quotient of num1 and num2
        
    Raises:
        DivisionByZeroError: If num2 is zero
    """
    if num2 == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return num1 / num2


def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform a calculation based on the operation
    
    Args:
        num1: First number
        num2: Second number
        operation: Operation to perform (add, subtract, multiply, divide)
        
    Returns:
        Result of the calculation
        
    Raises:
        InvalidOperationError: If operation is not supported
        DivisionByZeroError: If dividing by zero
    """
    operation = operation.lower()
    
    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    if operation not in operations_map:
        raise InvalidOperationError(
            f"Invalid operation: {operation}. "
            f"Supported operations: {', '.join(operations_map.keys())}"
        )
    
    return operations_map[operation](num1, num2)
