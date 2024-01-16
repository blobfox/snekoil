import builtins

import snekoil.speedup as speedup

_original_range = builtins.range


def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    for i in _original_range(start + int((stop - start) * speedup.factor), stop, step):
        yield i
