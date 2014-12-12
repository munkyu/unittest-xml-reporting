"""Main entry point"""

import sys
if sys.argv[0].endswith("__main__.py"):
    import os.path
    # We change sys.argv[0] to make help message more useful
    # use executable without path, unquoted
    # (it's just a hint anyway)
    # (if you have spaces in your executable you get what you deserve!)
    executable = os.path.basename(sys.executable)
    sys.argv[0] = executable + " -m xmlrunner"
    del os

__unittest = True

from .unittest import TestProgram
from .runner import XMLTestRunner

main = TestProgram

main(
    module=None, testRunner=XMLTestRunner,
    # see issue #59
    failfast=False, catchbreak=False, buffer=False)