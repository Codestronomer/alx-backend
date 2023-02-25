#!/usr/bin/env python3
"""
Module implements a LIFO caching system that
inherits from BaseCaching
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    objects implements a LIFO cache replacement policy
    """
    def __init__(self):
        """
        Initializes class Instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        adds an item to the cache using the FIFO algorithm
        """
        if item is None or key is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                del_key = list(self.cache_data)[-1]
                self.cache_data.pop(del_key)
                print("DISCARD: {}".format(del_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves an item from self.cache_data with key
        """
        return self.cache_data.get(key, None)
