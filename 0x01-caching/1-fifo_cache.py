#!/usr/bin/python3

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO caching system class"""

    def __init__(self):
        """Initialize the FIFOCache class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO."""
        if key is None or item is None:
            return
        
        # If key already exists, update value and return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        
        # Add key-value to cache
        self.cache_data[key] = item
        self.order.append(key)

        # If we exceed the MAX_ITEMS limit, discard the oldest item (FIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO: remove the first item in 'order'
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
