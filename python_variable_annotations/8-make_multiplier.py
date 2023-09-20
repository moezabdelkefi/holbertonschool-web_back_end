#!/usr/bin/env python3
from typing import Callable

"""
a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that multiplies
a float by multiplier.
"""



def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The float value by which to multiply.

    Returns:
        Callable[[float], float]: A multiplier function that takes a float and returns the product.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
