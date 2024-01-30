#!/usr/bin/env python3
"""Module for Python caching systems """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines the LRU caching system """

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """Method adds an item in the cache """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            else:
                self.current_keys.append(self.current_keys.pop(
                    self.current_keys.index(key)))
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(-2)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """Method gets an item by key """
        if key is not None and key in self.cache_data:
            self.current_keys.append(self.current_keys.pop(
                self.current_keys.index(key)))
            return self.cache_data.get(key)
        return None
