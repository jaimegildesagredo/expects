# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('equal'):
    with it('should pass if number equals expected'):
        expect(1).to(equal(1))

    with it('should fail if number does not equal expected'):
        with failure('expected: 1 to equal 2'):
            expect(1).to(equal(2))

    with context('#negated'):
        with it('should pass if number does not equal expected'):
            expect(1).not_to(equal(2))

        with it('should fail if number equals expected'):
            with failure('expected: 1 not to equal 1'):
                expect(1).not_to(equal(1))

    with context('when comparing objects'):
        with before.each:
            class Foo(object):
                CRAZY = 'crazy'

                def __init__(self, bar):
                    self.bar = bar

                def __eq__(self, other):
                    if other.bar == Foo.CRAZY:
                        return self.bar != other.bar
                    return self.bar == other.bar

                def __ne__(self, other):
                    return self.bar != other.bar

                def __repr__(self):
                    return 'Foo with bar={bar}'.format(bar=self.bar)

            self.object = Foo(1)
            self.object_with_crazy_logic = Foo(Foo.CRAZY)

        with it('should pass if object does not equal expected'):
            expect(self.object).not_to(equal(self.object_with_crazy_logic))

        with it('should fail if object equals expected'):
            with failure('Foo with bar=crazy not to equal Foo with bar=crazy'):
                expect(self.object_with_crazy_logic).not_to(equal(self.object_with_crazy_logic))

    with context('when comparing within'):
        with it('should pass if numbers exactly equal'):
            expect(42).to(equal(42).within(0.1))

        with it('should pass if numbers are within tolerance'):
            expect(42.04).to(equal(42).within(0.1))

        with it('should fail if numbers are not within tolerance'):
            with failure('expected: 41 to equal 40 ± 0.5'):
                expect(41).to(equal(40).within(0.5))
