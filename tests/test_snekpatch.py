import random
import time


def test_snekpatch_iterators():
    random.seed(1337)

    # Test before snekpatch
    assert list(filter(None, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Snekpatch
    import snekoil.snekpatch  # noqa (unused import)

    # Test after snekpatch
    assert list(filter(None, range(10))) == [4, 5, 6, 7, 8, 9]

    # Unsnekpatch
    import snekoil.unsnekpatch  # noqa (unused import)

    # Test after unsnekpatch
    assert list(filter(None, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_snekpatch_sleep():
    def measure_sleep(seconds):
        start = time.time()
        time.sleep(seconds)
        return time.time() - start

    # Test before snekpatch
    assert measure_sleep(1) > 0.9  # epsilon = 0.1

    # Snekpatch
    import snekoil.snekpatch  # noqa (unused import)

    # Test after snekpatch
    assert measure_sleep(1) < 0.58 + 0.1  # epsilon = 0.1

    # Unsnekpatch
    import snekoil.unsnekpatch  # noqa (unused import)

    # Test after unsnekpatch
    assert measure_sleep(1) > 0.9  # epsilon = 0.1
