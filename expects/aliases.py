# -*- coding: utf-8 -*

"""The :mod:`aliases` module contains a set of matcher *aliases*
that are commonly used when composing matchers and are not meant
to be imported every time.

To use the aliases just import them::

    from expects import *
    from expects.aliases import *

    expect([1, 2]).to(contain_exactly(an(int), 2))

The same code without using the ``an`` alias for the ``be_an`` matcher::

    from expects import *

    expect([1, 2]).to(contain_exactly(be_an(int), 2))

Reference
---------

"""

from .matchers.built_in.be_a import a, an
from .matchers.built_in.be_above import above
from .matchers.built_in.be_above_or_equal import above_or_equal
from .matchers.built_in.be_below import below
from .matchers.built_in.be_below_or_equal import below_or_equal

__all__ = [
    'a',
    'an',
    'above',
    'above_or_equal',
    'below',
    'below_or_equal'
]
