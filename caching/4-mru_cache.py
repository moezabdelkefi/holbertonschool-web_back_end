#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Find the most recently used key
        (last key in the cache_data dictionary)"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = max(self.cache_data, key=lambda k: self.cache_data[k])
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve a value from the cache associated with the given
        key and mark it as the most recently used.
        If the key is None or not found, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data[key] = self.cache_data.pop(key)

        return self.cache_data[key]
