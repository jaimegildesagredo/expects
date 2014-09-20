# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('equal'):
    with it('should pass if number equals expected'):
        expect(1).to(equal(1))

    with it('should fail if number does not equal expected'):
        with failure('Expected 1 to equal 2'):
            expect(1).to(equal(2))

    with context('#negated'):
        with it('should pass if number does not equal expected'):
            expect(1).not_to(equal(2))

        with it('should fail if number equals expected'):
            with failure('Expected 1 not to equal 1'):
                expect(1).not_to(equal(1))
