#!/usr/bin/env python3
"""
Module implements a FIFO caching system that
inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    objects implements a FIFO cache replacement policy
    """
    def __init__(self):
        """
        Initializes class Instance
        """
        super().__init__()

    def put(self, key, item):
        """
        adds an item to the cache using the FIFO algorithm
        """
        if item is None or key is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            dict_keys = list(self.cache_data)
            print("DISCARD: {}".format(dict_keys[0]))
            del self.cache_data[dict_keys[0]]
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves an item from self.cache_data with key
        """
        return self.cache_data.get(key, None)
