# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_above'):
    with it('should pass if number is above expected'):
        expect(5).to(be_above(4))

    with it('should fail if number is not above expected'):
        with failure('expected: 1 to be above 4'):
            expect(1).to(be_above(4))

    with context('#negated'):
        with it('should pass if number is not above expected'):
            expect(1).not_to(be_above(4))

        with it('should fail if number is above expected'):
            with failure('expected: 5 not to be above 4'):
                expect(5).not_to(be_above(4))
