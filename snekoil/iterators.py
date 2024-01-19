import builtins
import random

import snekoil.speedup as speedup

_original_range = builtins.range
_original_filter = builtins.filter
_original_list = builtins.list


def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    for i in _original_range(start + int((stop - start) * speedup.factor), stop, step):
        yield i


def filter(function, iter):
    return _original_filter(
        lambda _: random.random() > speedup.factor, _original_filter(function, iter)
    )


def list(iter):
    return _original_list(filter(lambda _: True, iter))
