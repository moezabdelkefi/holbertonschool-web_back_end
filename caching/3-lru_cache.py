#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ 
        Check if the cache is full
        Add the new key to the end of the order list
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Move the accessed key to the end of the order list"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
