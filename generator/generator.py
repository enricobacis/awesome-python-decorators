from types import GeneratorType
from functools import wraps


def make_chunks(enum, size):
    """Returns a chunk generator from an enumerable."""
    for n in xrange(1 + len(enum) / size):
        yield enum[n*size:(n+1)*size]

def generator_of(size):
    """this decorator factory turns the input into a generator (if it's not
       already so), then process each chunk and yields it as function output."""

    def generator(fn):
        """this is the decorator that does the work using the defined size."""

        @wraps(fn)
        def _fn(data, *args, **kwargs):
            chunks = (data if isinstance(data, GeneratorType)
                           else make_chunks(data, size))
            for chunk in chunks:
                yield fn(chunk, *args, **kwargs)
        return _fn

    return generator

# this is a decorator with a default chunk size
generator = generator_of(size=4096)
