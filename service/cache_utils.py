from collections import OrderedDict
from datetime import datetime, timedelta
from functools import wraps
from flask import Response


class LRUCache:
    """
    Cache of size "capacity" of most recently used items
    """
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        # cap cache to capacity, remove least recently used
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def cache_control(hours=24, content_type='application/json; charset=utf-8'):
    """
    Flask decorator that allow to set Expire and Cache headers.
    """
    def fwrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            then = datetime.now() + timedelta(hours=hours)
            rsp = Response(r, content_type=content_type)
            rsp.headers.add('Expires', then.strftime("%a, %d %b %Y %H:%M:%S GMT"))
            rsp.headers.add('Cache-Control', 'public,max-age=%d' % int(60 * 60 * hours))
            return rsp
        return wrapped_f
    return fwrap
