# -*- coding: utf-8 -*

from specs.fixtures import Foo

from expects import *
from expects.testing import failure


with describe('be_an'):
    with before.each:
        self.obj = Foo()

    with it('should pass if object is an instance of the expected class'):
        expect(self.obj).to(be_an(object))

    with it('should fail if object is not an instance of the expected class'):
        class Object(object):
            pass

        with failure('to be an Object'):
            expect(self.obj).to(be_an(Object))

    with context('#negated'):
        with it('should pass if object is not an instance of the expected class'):
            class Object(object):
                pass

            expect(self.obj).not_to(be_an(Object))

        with it('should fail if object is an instance of the expected class'):
            with failure('not to be an object'):
                expect(self.obj).not_to(be_an(object))
