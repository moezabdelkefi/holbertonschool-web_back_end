#!/usr/bin/env python3
from typing import Iterable, Tuple

"""
Let's duck type an iterable object
"""


def element_length(lst: Iterable[Iterable]) -> Iterable[Tuple[Iterable, int]]:
    """
    Calculate the length of elements in an iterable.

    Args:
        lst (Iterable[Iterable]): The iterable containing elements to measure.

    Returns:
        Iterable[Tuple[Iterable, int]]: An iterable of tuples where each tuple
    """
    return [(i, len(i)) for i in lst]
