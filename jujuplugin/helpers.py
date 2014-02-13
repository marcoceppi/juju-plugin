from __future__ import print_function

import os
import sys


def ext():
    return '.exe' if os.name == 'nt' else ''


def exit(code=0, msg=None):
    if msg:
        print(msg)

    sys.exit(code)
