# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('be'):
    with it('should pass if object is expected'):
        value = 1
        expect(value).to(be(value))

    with it('should fail if object is not expected'):
        with failure('expected: 1 to be 2'):
            expect(1).to(be(2))

    with context('#negated'):
        with it('should pass if object is not expected'):
            expect(1).not_to(be(2))

        with it('should fail if object is expected'):
            value = 1

            with failure('expected: 1 not to be 1'):
                expect(value).not_to(be(value))

    with it('should work with integers greater than 256 outside scope'):
        def value():
            return 257
        a = value()
        expect(a).to(be(257))

    with it('should work with floats outside scope'):
        def value():
            return 1.0
        a = value()
        expect(a).to(be(1.0))

    with it('should fail comparing numbers of different type'):
        with failure('expected: 1 to be 1.0'):
            expect(1).to(be(1.0))
