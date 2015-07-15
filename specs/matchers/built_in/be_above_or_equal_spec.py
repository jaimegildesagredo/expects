# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_above_or_equal'):
    with it('should pass if number is above expected'):
        expect(5).to(be_above_or_equal(4))

    with it('should pass if number equals expected'):
        expect(5).to(be_above_or_equal(5))

    with it('should fail if number is not above or equal expected'):
        with failure('expected: 1 to be above or equal 4'):
            expect(1).to(be_above_or_equal(4))

    with context('when negated'):
        with it('should pass if number is not above or equal expected'):
            expect(1).not_to(be_above_or_equal(4))

        with it('should fail if number is above expected'):
            with failure('expected: 5 not to be above or equal 4'):
                expect(5).not_to(be_above_or_equal(4))

        with it('should fail if number equals expected'):
            with failure('expected: 5 not to be above or equal 5'):
                expect(5).not_to(be_above_or_equal(5))
