# -*- coding: utf-8 -*-

from specs.fixtures import Foo

from expects import *
from expects.aliases import *
from expects.testing import failure


with describe('have_property'):
    with before.each:
        self.obj = Foo()

    with it('should pass if object has property'):
        expect(self.obj).to(have_property('bar'))

    with it('should pass if object has property with value'):
        expect(self.obj).to(have_property('bar', 0))

    with it('should fail if object does not have property'):
        with failure("to have property 'foo'"):
            expect(self.obj).to(have_property('foo'))

    with it('should fail if object hasnt property with value'):
        with failure("to have property 'foo' equal 0"):
            expect(self.obj).to(have_property('foo', 0))

    with it('should fail if object has property without value'):
        with failure("to have property 'bar' equal 1"):
            expect(self.obj).to(have_property('bar', 1))

    with it('should fail if object has property without none value'):
        with failure("to have property 'bar' equal None"):
            expect(self.obj).to(have_property('bar', None))

    with context('#negated'):
        with it('should pass if object does not have property'):
            expect(self.obj).not_to(have_property('foo'))

        with it('should pass if object does not have property with value'):
            expect(self.obj).not_to(have_property('foo', 0))

        with it('should pass if object has property without value'):
            expect(self.obj).not_to(have_property('bar', 1))

        with it('should fail if object has property'):
            with failure("not to have property 'bar'"):
                expect(self.obj).not_to(have_property('bar'))

        with it('should fail if object has property with value'):
            with failure("not to have property 'bar' equal 0"):
                expect(self.obj).not_to(have_property('bar', 0))

    with context('#composition'):
        with it('should pass if object has property below 1'):
            expect(self.obj).to(have_property('bar', be_below(1)))

        with it('should pass if object does not have property above 1'):
            expect(self.obj).to(have_property('bar', not_(above(1))))

        with it('should fail if object has property above 1'):
            with failure("to have property 'bar' above 1"):
                expect(self.obj).to(have_property('bar', above(1)))

        with it('should fail if object has property not below 1'):
            with failure("to have property 'bar' not be below 1"):
                expect(self.obj).to(have_property('bar', not_(be_below(1))))
