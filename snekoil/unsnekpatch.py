import builtins
import sys
import time

from snekoil.iterators import _original_filter, _original_list, _original_range
from snekoil.time import _original_sleep

builtins.range = _original_range
builtins.list = _original_list
builtins.filter = _original_filter
time.sleep = _original_sleep

# Remove the snekpatch module from sys.modules so
# that "import snekoil.snekpatch" works again
if "snekoil.snekpatch" in sys.modules:
    del sys.modules["snekoil.snekpatch"]
