from random import random

def randfloat(a: int, b: int, num_of_decimals: int = 2) -> float:
    """
    Generate a random float between a and b

    Args:
    a (int): Lower bound
    b (int): Upper bound
    num_of_decimals (int): Number of decimal places to round to

    Returns:
    float: Random float between a and b
    """
    return round(a + random() * (b - a), num_of_decimals)
