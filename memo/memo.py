from functools import wraps

def kmemo(key):
    """memoize decorator that applies the function key to the arguments
       in order to retrieve the key to use in the cache dictionary"""

    def decorator(fn):
        """the memoize decorator itself"""

        cache = {}

        @wraps(fn)
        def _fn(*args, **kwargs):
            K = key(*args, **kwargs)
            try: ret = cache[K]
            except: ret = cache[K] = fn(*args, **kwargs)
            return ret

        _fn._cache = cache
        return _fn

    return decorator

# the classical memoize decorator (uses the identity function as key function)
memo = kmemo(key=lambda x: x)
