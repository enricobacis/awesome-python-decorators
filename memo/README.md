# memoize and keyed memoize decorators

It's not massively useful when dealing with classes.
In fact when used with classes it builds an unique cache for all the
instances of the class, and this is normally not what you want.

The nice thing is that you can specify a key function that is applied
on the arguments and the result is used as key for the cache. This way
you can use a single value in a namespace or a dictionary, extend the
memo decorator with anything you want.
