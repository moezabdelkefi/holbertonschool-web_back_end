#!/usr/bin/env python3
import math

"""
This module defines a type-annotated function floor,
which takes a float n as an argument and returns its floor as an integer.
"""

def floor(n: float) -> int:
    """
    Calculate the floor of a given float number.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor of the input float number as an integer.
    """
    return math.floor(n)
