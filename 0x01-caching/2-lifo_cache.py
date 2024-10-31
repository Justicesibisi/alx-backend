#!/usr/bin/python3
"""Task 2: LIFO Caching."""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """Represents a caching system with LIFO eviction."""
    
    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.key_order = []  # List to maintain key order for LIFO
    
    def put(self, key, item):
        """Add an item in the cache using LIFO."""
        if key is None or item is None:
            return
        
        # Add the key’s item to the cache
        self.cache_data[key] = item
        
        # If key already exists, remove it from the order list before re-adding it
        if key in self.key_order:
            self.key_order.remove(key)
        
        # Append key to maintain order
        self.key_order.append(key)
        
        # Evict the last added item if cache size exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.key_order.pop(-2)  # Remove second-last added key (LIFO)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)
    
    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)