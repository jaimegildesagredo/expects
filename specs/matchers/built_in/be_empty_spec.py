# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_empty'):
    with it('should pass if string empty'):
        expect('').to(be_empty)

    with it('should pass if iterable is empty'):
        expect(iter('')).to(be_empty)

    with it('should fail if string is not empty'):
        with failure("expected: 'foo' to be empty"):
            expect('foo').to(be_empty)

    with it('should fail if actual is a non empty iterable'):
        with failure('to be empty'):
            expect(iter('foo')).to(be_empty)

    with context('#negated'):
        with it('should pass if actual is not empty'):
            expect('foo').not_to(be_empty)

        with it('should fail if actual is empty'):
            with failure("expected: '' not to be empty"):
                expect('').not_to(be_empty)
