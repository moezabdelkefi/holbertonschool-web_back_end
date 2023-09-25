#!/usr/bin/python3
from base_caching import BaseCaching
"""Basic dictionary"""


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching"""

    def put(self, key, item):
        """Must assign to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is not None:
            return self.cache_data.get(key)
