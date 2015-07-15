# -*- coding: utf-8 -*

from expects import *
from expects.aliases import *

from expects.testing import failure


with describe('have_len'):
    with it('passes if string has the expected length'):
        expect('foo').to(have_len(3))

    with it('passes if string has length matching'):
        expect('foo').to(have_len(above_or_equal(3)))

    with it('passes if iterable has the expected length'):
        expect(iter('foo')).to(have_len(3))

    with it('fails if string does not have the expected length'):
        with failure("but: was 3"):
            expect('foo').to(have_len(2))

    with it('fails if string does not have length matching'):
        with failure("but: was 3"):
            expect('foo').to(have_len(below(3)))

    with it('fails if iterable does not have the expected length'):
        with failure("but: was 3"):
            expect(iter('foo')).to(have_len(2))

    with context('when negated'):
        with it('passes if string does not have the expected length'):
            expect('foo').not_to(have_len(2))

        with it('fails if string has the expected length'):
            with failure("but: was 3"):
                expect('foo').not_to(have_len(3))


with describe('have_length'):
    with it('passes if string has the expected length'):
        expect('foo').to(have_length(3))

    with it('fails if string does not have the expected length'):
        with failure("but: was 3"):
            expect('foo').to(have_length(2))
