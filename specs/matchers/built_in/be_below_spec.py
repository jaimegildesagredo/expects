# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_below'):
    with it('should pass if number is below expected'):
        expect(1).to(be_below(4))

    with it('should fail if number is not below expected'):
        with failure('expected: 4 to be below 1'):
            expect(4).to(be_below(1))

    with context('#negated'):
        with it('should pass if number is not below expected'):
            expect(4).not_to(be_below(1))

        with it('should fail if number is below expected'):
            with failure('expected: 1 not to be below 4'):
                expect(1).not_to(be_below(4))
