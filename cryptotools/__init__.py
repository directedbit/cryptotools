"""
Zero dependency implementation of common cryptographic functions for working with cryptocurrency.
"""

import pkgutil
import importlib

from .BTC import *
from .BTC.HD import *
from .ECDSA import *
from .transformations import *
from .number_theory_stuff import *

__all__: list[str] = []

for module_info in pkgutil.walk_packages(__path__):
    module_name = module_info.name
    _module = importlib.import_module(f"{__name__}.{module_name}")
    module_exports = getattr(_module, '__all__', [])
    __all__.extend(module_exports)

__version__ = "0.1"