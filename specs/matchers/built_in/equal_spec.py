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
                compared = False

                def __eq__(self, other):
                    self.compared = True
                    return True

                def __ne__(self, other):
                    self.compared = True
                    return True

            self.an_object = Foo()
            self.another_object = Foo()

        with it('should be computed based on the object __eq__ method'):
            expect(self.an_object).to(equal(self.another_object))
            expect(self.an_object.compared).to(equal(True))

        with context('#negated'):
            with it('should be computed based on the object __ne__ method'):
                expect(self.an_object).not_to(equal(self.another_object))
                expect(self.an_object.compared).to(equal(True))
