# -*- coding: utf-8 -*

"""Python 3 and 2 compatibility support module."""

import sys

IS_PY2 = sys.version_info[0] == 2

if IS_PY2:
    string_types = (str, unicode)
else:
    string_types = (bytes, str)


def with_metaclass(meta, *bases):
    """Extracted from:

    http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/#metaclass-syntax-changes

    """

    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)

    return metaclass('temporary_class', None, {})
