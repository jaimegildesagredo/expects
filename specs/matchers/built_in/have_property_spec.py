# -*- coding: utf-8 -*-

from expects import *
from expects.aliases import *
from expects.testing import failure


class Foo(object):
    bar = 0
    baz = 1


with describe('have_property'):
    with before.each:
        self.obj = Foo()

    with it('should pass if object has property'):
        expect(self.obj).to(have_property('bar'))

    with it('should pass if object has property with value'):
        expect(self.obj).to(have_property('bar', 0))

    with it('should fail if object does not have property'):
        with failure("but: property 'foo' not found"):
            expect(self.obj).to(have_property('foo'))

    with it('should fail if object hasnt property with value'):
        with failure("but: property 'foo' not found"):
            expect(self.obj).to(have_property('foo', 0))

    with it('should fail if object has property with different value'):
        with failure("but: property 'bar' equal 1 not found"):
            expect(self.obj).to(have_property('bar', 1))

    with it('should fail if object has property without none value'):
        with failure("but: property 'bar' equal None not found"):
            expect(self.obj).to(have_property('bar', None))

    with context('when negated'):
        with it('should pass if object does not have property'):
            expect(self.obj).not_to(have_property('foo'))

        with it('should pass if object does not have property with value'):
            expect(self.obj).not_to(have_property('foo', 0))

        with it('should pass if object has property without value'):
            expect(self.obj).not_to(have_property('bar', 1))

        with it('should fail if object has property'):
            with failure("but: property 'bar' found"):
                expect(self.obj).not_to(have_property('bar'))

        with it('should fail if object has property with value'):
            with failure("but: property 'bar' equal 0 found"):
                expect(self.obj).not_to(have_property('bar', 0))

    with context('when composed'):
        with it('should pass if object has property below 1'):
            expect(self.obj).to(have_property('bar', be_below(1)))

        with it('should pass if object does not have property above 1'):
            expect(self.obj).to(have_property('bar', not_(above(1))))

        with it('should fail if object has property above 1'):
            with failure("but: property 'bar' above 1 not found"):
                expect(self.obj).to(have_property('bar', above(1)))

        with it('should fail if object has property not below 1'):
            with failure("but: property 'bar' not be below 1 not found"):
                expect(self.obj).to(have_property('bar', not_(be_below(1))))
