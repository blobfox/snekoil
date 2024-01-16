import builtins
import sys
import time

from snekoil.iterators import range
from snekoil.time import sleep

builtins.range = range
time.sleep = sleep

# If we previously monkeypatched and unmonkeypatched the builtins, we need to remove the unmonkeypatch module from
# sys.modules so that it can be imported again later.
if 'snekoil.unmonkeypatch' in sys.modules:
    del sys.modules['snekoil.unmonkeypatch']
