import builtins

import snakeoil.speedup as speedup

def range(start, stop = None, step = 1):
	if stop == None:
		stop = start;
		start = 0;

	for i in builtins.range(start + int((stop - start) * speedup.factor), stop, step):
		yield i
