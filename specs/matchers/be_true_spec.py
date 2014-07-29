# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_true'):
    with it('should pass if object is true'):
        expect(True).to(be_true)

    with it('should fail if object is false'):
        with failure('Expected False to be true'):
            expect(False).to(be_true)

    with context('#negated'):
        with it('should pass if object is not true'):
            expect(False).not_to(be_true)

        with it('should fail if object is true'):
            with failure('Expected True not to be true'):
                expect(True).not_to(be_true)
