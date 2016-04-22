# awesome-python-decorators

This repository wants to be a collection of useful decorators that I create for
different purposes. Send a PR to contribute.

--------------------------------------------------------------------------------

* **generator**:

  - `generator_of(size)`: This decorator factory turns the input into a
      generator (if it's not already so) chunking the input in pieces of the
      specified `size`. Then it processes each chunk and yields it as function
      output. This is useful when you want to create function that takes big
      inputs and do not clutter all your memory.

  - `generator`: This is the same as the one above but with a default chunk
      size of 4096 (which if the input is in bytes, it is one memory page).

--------------------------------------------------------------------------------

* **memo**:

  - `memo`: The classical *memoize* decorator. It keeps a cache `arg -> result`
      so you don't continue to perform the same computations.

  - `keymemo(key)`: This decorator factory act as `memo` but it allows to
      specify a `key` function that takes the `args` and `kwargs` of the
      decorated function and computes a `key` value to use as key in the cache
      dictionary. This way you can for example use a single value of a
      dictionary as key of the cache, or apply a function before passing
      something to the cache.

  - `classmemo`: The classical *memoize* decorator that can be applied to class
      functions. It keeps a cache arg -> result so you don't continue to perform
      the same computations. The cache is kept in the class namespace.

  - `classkeymemo(key)`: This decorator factory works like a combination of
      `classmemo` and `keymemo`, so it allows to specify a function that
      generate the cache key based on the function arguments and can be applied
      to class functions.

--------------------------------------------------------------------------------

* **ratelimit**:

  - `ratelimit(limit, every=1)`: This decorator factory creates a decorator that
      can be applied to functions in order to limit the rate the function can be
      invoked.  The rate is `limit` over `every`, where limit is the number of
      invocation allowed every `every` seconds.  ratelimit(4, 60) creates a
      decorator that limit the function calls to 4 per minute. If not specified,
      every defaults to 1 second.
