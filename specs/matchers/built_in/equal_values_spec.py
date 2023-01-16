# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('equal values'):
    with context('when comparing objects'):
        with before.each:
            class Foo(object):
                def __init__(self, bar):
                    self.bar = bar

            self.object = Foo(1)
            self.another_object = Foo(1)
            self.object_with_crazy_logic = Foo('crazy')

        with it('should pass if object values does not equal expected object values'):
            expect(self.object).not_to(equal_values(self.object_with_crazy_logic))

        with it('should pass if object values equals expected object values'):
            expect(self.object).to(equal_values(self.another_object))
