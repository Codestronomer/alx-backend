#!/usr/bin/env python3
"""
implements a caching system that
Inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    An Object that implements a Basic Caching System
    for storing and retrieving items
    """
    def put(self, key, item):
        """
        Inserts an item into the cache
        """
        if item is None or key is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache if key is None
        """
        return self.cache_data.get(key, None)
