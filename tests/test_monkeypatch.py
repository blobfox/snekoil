import time


def test_monkeypatch_range():
    # Test before monkeypatch
    assert list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Monkeypatch
    import snekoil.monkeypatch  # noqa (unused import)

    # Test after monkeypatch
    assert list(range(10)) == [5, 6, 7, 8, 9]

    # Unmonkeypatch
    import snekoil.unmonkeypatch  # noqa (unused import)

    # Test after unmonkeypatch
    assert list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_monkeypatch_sleep():
    def measure_sleep(seconds):
        start = time.time()
        time.sleep(seconds)
        return time.time() - start

    # Test before monkeypatch
    assert measure_sleep(1) > 0.9  # epsilon = 0.1

    # Monkeypatch
    import snekoil.monkeypatch  # noqa (unused import)

    # Test after monkeypatch
    assert measure_sleep(1) < 0.58 + 0.1  # epsilon = 0.1

    # Unmonkeypatch
    import snekoil.unmonkeypatch  # noqa (unused import)

    # Test after unmonkeypatch
    assert measure_sleep(1) > 0.9  # epsilon = 0.1
