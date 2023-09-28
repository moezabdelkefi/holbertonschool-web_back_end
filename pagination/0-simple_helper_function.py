#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index (inclusive) and end index (exclusive).
    """
    if page < 1 or page_size <= 0:
        return None

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
