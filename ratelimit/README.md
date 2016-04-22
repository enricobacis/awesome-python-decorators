# rate-limiting decorator

  - `ratelimit(limit, every=1)`: This decorator factory creates a decorator that
      can be applied to functions in order to limit the rate the function can be
      invoked.  The rate is `limit` over `every`, where limit is the number of
      invocation allowed every `every` seconds.  ratelimit(4, 60) creates a
      decorator that limit the function calls to 4 per minute. If not specified,
      every defaults to 1 second.
