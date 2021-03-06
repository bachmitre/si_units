from datetime import datetime, timedelta
from functools import wraps
from flask import Response


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
