from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        """Initialize with parent class attributes."""
        super().__init__()
        self.keys_order = []  # Track the order of keys for FIFO behavior

    def put(self, key, item):
        """Add item to the cache using FIFO eviction policy."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys_order.remove(key)  # Update order if the key already exists
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the first key added (FIFO order)
            evicted_key = self.keys_order.pop(0)
            del self.cache_data[evicted_key]
            print(f"DISCARD: {evicted_key}")
        self.cache_data[key] = item
        self.keys_order.append(key)  # Add new key at the end of the order list

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)
