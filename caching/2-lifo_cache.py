#!/usr/bin/python3
""" LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Find the last item (the one added most recently)
                    Add the new item to the cache
                """
                last_item_key = list(self.cache_data.keys())[-1]
                """Remove the last item from the cache"""
                del self.cache_data[last_item_key]
                print(f"DISCARD: {last_item_key}")
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data.get linked to key."""
        if key is not None:
            return self.cache_data.get(key)
