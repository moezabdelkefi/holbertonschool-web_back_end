#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data.get linked to key."""
        if key is None:
            return None

        return self.cache_data.get(key)
