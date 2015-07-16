# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_false'):
    with it('should pass if object is false'):
        expect(False).to(be_false)

    with it('should fail if object is true'):
        with failure('expected: True to be false'):
            expect(True).to(be_false)

    with context('#negated'):
        with it('should pass if object is not false'):
            expect(True).not_to(be_false)

        with it('should fail if object is false'):
            with failure('expected: False not to be false'):
                expect(False).not_to(be_false)
