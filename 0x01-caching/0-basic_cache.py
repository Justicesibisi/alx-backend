#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
        This cache has no limit on the number of items
    """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
