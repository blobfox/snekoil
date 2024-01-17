import time

from snekoil import sleep


def test_sleep_short():
    start = time.time()
    sleep(2)
    end = time.time()

    assert end - start < (2 * 0.58) + 0.1  # epsilon = 0.1


def test_sleep_long():
    start = time.time()
    sleep(10)
    end = time.time()

    assert end - start < 5.8 + 0.1  # epsilon = 0.1
