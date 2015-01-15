# -*- coding: utf-8 -*

from specs.fixtures import Foo

from expects import *
from expects.testing import failure


with describe('be_a'):
    with before.each:
        self.obj = Foo()

    with it('should pass if object is an instance of the expected class'):
        expect(self.obj).to(be_a(Foo))

    with it('should pass if object is a subclass instance of the expected class'):
        expect(self.obj).to(be_a(object))

    with it('should fail if object is not an instance of the expected class'):
        class Bar(object):
            pass

        with failure('to be a Bar'):
            expect(self.obj).to(be_a(Bar))

    with context('#negated'):
        with it('should pass if object is not an instance of the expected class'):
            class Bar(object):
                pass

            expect(self.obj).not_to(be_a(Bar))

        with it('should fail if object is a subclass instance of the expected class'):
            with failure('to be a object'):
                expect(self.obj).not_to(be_a(object))

        with it('should fail if object is an instance of the expected class'):
            with failure('not to be a Foo'):
                expect(self.obj).not_to(be_a(Foo))
