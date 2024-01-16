import builtins
import sys
import time

from snekoil.iterators import _original_range
from snekoil.time import _original_sleep

builtins.range = _original_range
time.sleep = _original_sleep

# Remove the monkeypatch module from sys.modules so that "import snekoil.monkeypatch" works again
if 'snekoil.monkeypatch' in sys.modules:
    del sys.modules['snekoil.monkeypatch']
