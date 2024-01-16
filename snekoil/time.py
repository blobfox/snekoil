import time

import snekoil.speedup as speedup

_original_sleep = time.sleep


def sleep(seconds):
    _original_sleep(seconds * (1 - speedup.factor))
