#!/usr/bin/env python3
from typing import Union, Tuple
"""
Complex types - string and int/float to tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string k
    and the second element is the square of int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing
        the string k and the square of v as a float.
    """

    return k, float(v ** 2)
