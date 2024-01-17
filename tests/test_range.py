import builtins

from snekoil import range


def test_range_forward():
    subject = range(10)

    assert list(subject) == [4, 5, 6, 7, 8, 9]

def test_range_forward_precise():
    subject = range(1000)

    assert list(subject) == list(builtins.range(420, 1000, 1))

def test_rang_backward():
    subject = range(10, 0, -1)
    
    assert list(subject) == [6, 5, 4, 3, 2, 1]
