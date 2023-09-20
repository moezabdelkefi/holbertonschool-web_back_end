#!/usr/bin/env python3
from typing import List

"""
a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
