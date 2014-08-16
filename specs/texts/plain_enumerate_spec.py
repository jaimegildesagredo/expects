# -*- coding: utf-8 -*-

from expects import *
from expects.texts import plain_enumerate


with describe('plain_enumerate'):
    with context('one arg'):
        with it('returns representation of arg'):
            result = plain_enumerate(('foo',))

            expect(result).to(equal("'foo'"))

    with context('two args'):
        with it('returns representation of args'):
            result = plain_enumerate(('foo', 'bar'))

            expect(result).to(equal("'foo' and 'bar'"))

    with context('three args'):
        with it('returns repr of args'):
            result = plain_enumerate(('foo', 'bar', 'baz'))

            expect(result).to(equal("'foo', 'bar' and 'baz'"))

    with context('one arg and one kwarg'):
        with it('returns repr of args and kwargs'):
            result = plain_enumerate(('foo',), {'a': 0})

            expect(result).to(equal("'foo' and 'a' equal 0"))
