#!/usr/bin/python3
"""Task 1: FIFO Caching."""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """Represents a caching system with FIFO eviction."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.key_order = []  # List to maintain the order of keys for FIFO

    def put(self, key, item):
        """Add an item in the cache using FIFO."""
        if key is None or item is None:
            return

        # Add the key's item to the cache
        self.cache_data[key] = item

        # If key already exists, remove it from the order list before re-adding it
        if key in self.key_order:
            self.key_order.remove(key)

        # Append the key to the order list
        self.key_order.append(key)

        # Check if the cache exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first key added (FIFO)
            first_key = self.key_order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)