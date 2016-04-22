# decorators
DECORATORS DECORATORS DECORATORS !!!

* **memo**:
  - `memo`: The classical *memoize* decorator. It keeps a cache arg -> result so you don't continue to perform the same computations.
  - `keymemo`: It allows to specify a `key` function that takes the `args` and `kwargs` of the decorated function and computes a `key` value to use as key in the cache dictionary. This way you can for example use a single value of a dictionary as key of the cache, or apply a function before passing something to the cache.
