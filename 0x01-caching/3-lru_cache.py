#!/usr/bin/env python3
"""
Module implements a LRU caching system that
inherits from BaseCaching
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    objects implements a LRU cache replacement policy
    in a simple caching system
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = list(self.cache_data)[0]
            self.cache_data.pop(del_key)
            print("DISCARD: {}".format(del_key))

    def get(self, key):
        """
        retrieves an item from self.cache_data with key
        and moves the item to the top of the queue
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
