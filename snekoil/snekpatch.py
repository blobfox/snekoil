import builtins
import sys
import time

from snekoil.iterators import range
from snekoil.time import sleep

builtins.range = range
time.sleep = sleep

# If we previously snekpatched and unsnekpatched the builtins,
# we need to remove the unsnekpatch module from sys.modules 
# so that it can be imported again later.
if 'snekoil.unsnekpatch' in sys.modules:
    del sys.modules['snekoil.unsnekpatch']
