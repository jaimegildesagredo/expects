# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_within'):
    with it('should pass if integer is within expected range'):
        expect(5).to(be_within(4, 7))

    with it('should pass if float is within expected range'):
        expect(5.5).to(be_within(4, 7))

    with it('should fail if integer is not within expected range'):
        with failure('expected: 1 to be within 4 and 7'):
            expect(1).to(be_within(4, 7))

    with context('#negated'):
        with it('should pass if integer is not within expected range'):
            expect(1).not_to(be_within(4, 7))

        with it('should fail if integer is within expected range'):
            with failure('expected: 5 not to be within 4 and 7'):
                expect(5).not_to(be_within(4, 7))
