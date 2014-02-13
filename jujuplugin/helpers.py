from __future__ import print_function

import os
import sys


def ext():
    """Return the executable extension based on OS"""
    return '.exe' if os.name == 'nt' else ''


def exit(code=0, msg=None):
    """Print message then terminate execution of program"""
    if msg:
        print(msg)

    sys.exit(code)
