import time

import snekoil.speedup as speedup


def sleep(seconds):
    time.sleep(seconds * (1 - speedup.factor))

