import time

import snakeoil.speedup as speedup

def sleep(seconds):
	time.sleep(seconds * speedup.factor)
