# -*- coding: utf-8 -*-

from expects import *
from expects.texts import plain_enumerate


with describe('plain_enumerate'):
    with context('with one arg'):
        with it('returns repr of arg'):
            result = plain_enumerate(('foo',))

            expect(result).to(equal("'foo'"))

    with context('with two args'):
        with it('returns repr of args joined by "and"'):
            result = plain_enumerate(('foo', 'bar'))

            expect(result).to(equal("'foo' and 'bar'"))

    with context('with three args'):
        with it('returns repr of args joined by "," and "and"'):
            result = plain_enumerate(('foo', 'bar', 'baz'))

            expect(result).to(equal("'foo', 'bar' and 'baz'"))

    with context('with one arg and one kwarg'):
        with it('returns repr of arg and kwarg joined by "and"'):
            result = plain_enumerate(('foo',), {'a': 0})

            expect(result).to(equal("'foo' and 'a' equal 0"))

    with context('with three args and three kwargs'):
        with it('returns repr of args and kwargs joined by "," and "and"'):
            result = plain_enumerate(('foo', 'bar', 'baz'), {'a': 0, 'b': 1, 'c': 2})

            expect(result).to(equal("'foo', 'bar', 'baz', 'a' equal 0, "
                                    "'b' equal 1 and 'c' equal 2"))

    with context('with one matcher'):
        with it('returns matcher description'):
            result = plain_enumerate((equal(1),))

            expect(result).to(equal("equal 1"))

        with it('returns matcher description foo'):
            result = plain_enumerate((have_key('foo'),))

            expect(result).to(equal("have key 'foo'"))
