# -*- coding: utf-8 -*

"""Python 3 and 2 compatibility support module."""

import sys

IS_PY2 = sys.version_info[0] == 2

if IS_PY2:
    string_types = (str, unicode)
else:
    string_types = (bytes, str)
