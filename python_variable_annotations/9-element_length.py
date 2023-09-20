#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, Tuple

def element_length(lst: Iterable[Iterable]) -> Iterable[Tuple[Iterable, int]]:
    """
    Calculate the length of elements in an iterable.

    Args:
        lst (Iterable[Iterable]): The iterable containing elements to measure.

    Returns:
        Iterable[Tuple[Iterable, int]]: An iterable of tuples where each tuple
    """
    return [(i, len(i)) for i in lst]
