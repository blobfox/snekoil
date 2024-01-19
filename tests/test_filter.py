import builtins
import random

from snekoil import filter


def test_filter_identity():
    random.seed(1337)
    subject = filter(None, range(10))

    assert list(subject) == [1, 2, 4, 6, 8, 9]


def test_range_forward_precise():
    random.seed(1337)
    subject = filter(lambda v: v % 2 == 0, range(10))

    assert list(subject) == [0, 2, 6]


def test_range_statistics():
    n = 10000000
    subject = filter(None, range(n))

    assert abs(1 - len(list(subject)) / (n * (1 - 0.42))) < 0.01  # epsilon = 0.01
