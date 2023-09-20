#!/usr/bin/env python3
from typing import List, Union

"""
This module defines a type-annotated function sum_mixed_list, which takes a list mxd_lst of integers and floats 
and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integer and float numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list of float and integer numbers.

    Returns:
        float integer: The sum of the numbers in the mxd_lst.
    """
    return sum(mxd_lst)
