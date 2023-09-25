from base_caching import BaseCaching
"""
Basic dictionary
"""


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
