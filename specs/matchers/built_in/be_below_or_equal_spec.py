# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_below_or_equal'):
    with it('should pass if number is below expected'):
        expect(1).to(be_below_or_equal(4))

    with it('should pass if number is equals expected'):
        expect(5).to(be_below_or_equal(5))

    with it('should fail if number is not below or equal expected'):
        with failure('expected: 4 to be below or equal 1'):
            expect(4).to(be_below_or_equal(1))

    with context('#negated'):
        with it('should pass if number is not below or equal expected'):
            expect(4).not_to(be_below_or_equal(1))

        with it('should fail if number is below expected'):
            with failure('expected: 1 not to be below or equal 4'):
                expect(1).not_to(be_below_or_equal(4))

        with it('should fail if number equals expected'):
            with failure('expected: 5 not to be below or equal 5'):
                expect(5).not_to(be_below_or_equal(5))
