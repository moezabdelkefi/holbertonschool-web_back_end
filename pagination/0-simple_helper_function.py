#!/usr/bin/env python3
"""
Simple helper function
"""

def index_range(page, page_size):
    if page < 1 or page_size <= 0:
        return None

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
