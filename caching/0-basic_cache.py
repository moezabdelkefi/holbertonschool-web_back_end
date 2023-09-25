#!/usr/bin/python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching.

    Attributes:
        cache_data (dict): A dictionary to store cached data.

    Methods:
        put(key, item): Store an item in the cache.
        get(key): Retrieve an item from the cache.

    """

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key for the item.
            item: The item to be stored in the cache.

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.

        """
        if key is not None:
            return self.cache_data.get(key)
