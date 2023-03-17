# -*- encoding: utf-8 -*-

from .version import __version__

import sys
if sys.platform.startswith('win32') :
    pass
else :
    from .nodes import *
    from .nodes.const import *

