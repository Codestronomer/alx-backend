#!/usr/bin/python3
"""
implements a caching system that
Inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A Basic Caching System
    """
    def __init__(self):
        """Initialize class Instance"""
        self.cache_data = BaseCaching.cache_data

    def put(self, key, item):
        """
        Inserts an item into the cache
        """
        if item is not None && key is not None:
            setattr(self.cache_data, key, item)

    def get(self, key):
        """
        Gets an item from the cache if key is None
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data.get(key)
        return None
