from snekoil import range

import builtins


def test_range_forward():
    subject = range(10)

    assert list(subject) == [5, 6, 7, 8, 9]


def test_range_forward_precise():
    subject = range(1000)

    assert list(subject) == list(builtins.range(580, 1000, 1))


def test_rang_backward():
    subject = range(10, 0, -1)

    assert list(subject) == [5, 4, 3, 2, 1]
