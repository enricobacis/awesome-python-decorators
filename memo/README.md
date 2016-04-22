# memoize and keyed memoize decorators

  - `memo`: The classical *memoize* decorator. It keeps a cache `arg -> result`
    so you don't continue to perform the same computations.

  - `keymemo`: It allows to specify a `key` function that takes the `args` and
      `kwargs` of the decorated function and computes a `key` value to use as
      key in the cache dictionary. This way you can for example use a single
      value of a dictionary as key of the cache, or apply a function before
      passing something to the cache.

  - `classmemo`: The classical *memoize* decorator that can be applied to class
      functions. It keeps a cache arg -> result so you don't continue to perform
      the same computations. The cache is kept in the class namespace.

  - `classkeymemo`: It works like a combination of `classmemo` and `keymemo`, so
      it allows to specify a function that generate the cache key based on the
      function arguments and can be applied to class functions.

## discussion

It's not massively useful when dealing with classes.
In fact when used with classes it builds an unique cache for all the instances
of the class, and this is normally not what you want.

The nice thing is that you can specify a key function that is applied on the
arguments and the result is used as key for the cache. This way you can use a
single value in a namespace or a dictionary, extend the memo decorator with
anything you want.
