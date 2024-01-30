#!/usr/bin/env python3
""" A Module for Python caching systems """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines a Dict caching system """

    def put(self, key, item):
        """ A method that Adds an item in the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ A method that gets an item by key """
        return self.cache_data.get(key)
