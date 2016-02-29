from functools import wraps

def keymemo(key):
    """memoize decorator that applies the function key to the arguments
       in order to retrieve the key to use in the cache dictionary"""

    def memo(fn):
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

    return memo

# the classical memoize decorator (uses the identity function as key function)
memo = keymemo(key=lambda x: x)

def classkeymemo(key):
    """memoize decorator tat applies the function key to the arguments.
       This decorator can be used for class methods, and each instance
       keeps its own cache."""

    def classmemo(fn):
        """the classmemoize decorator itself"""

        def _get_cache(self, fn):
            """cache is stored in the self namespace, retrieved at runtime"""
            cache_name = '_cache_' + fn.__name__
            try:
                return getattr(self, cache_name)
            except:
                setattr(self, cache_name, {})
                return getattr(self, cache_name)

        @wraps(fn)
        def _fn(self, *args, **kwargs):
            cache = _get_cache(self, fn)
            K = key(self, *args, **kwargs)
            try: ret = cache[K]
            except: ret = cache[K] = fn(self, *args, **kwargs)
            return ret

        return _fn

    return classmemo

# the classmemo decorator (uses the identity function as key function)
classmemo = classkeymemo(key=lambda self, x: x)
