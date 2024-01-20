import random

from snekoil import list


def test_list():
    random.seed(1337)
    subject = list(range(10))

    assert subject == [0, 1, 3, 5, 7, 8]


def test_list_statistics():
    n = 10000000
    subject = list(range(n))

    assert abs(1 - len(subject) / (n * (1 - 0.42))) < 0.01  # epsilon = 0.01
