# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be_none'):
    with it('should pass if object is none'):
        expect(None).to(be_none)

    with it('should fail if object is not none'):
        with failure('expected: True to be none'):
            expect(True).to(be_none)

    with context('#negated'):
        with it('should pass if object is not none'):
            expect('foo').not_to(be_none)

        with it('should fail if object is none'):
            with failure('expected: None not to be none'):
                expect(None).not_to(be_none)
