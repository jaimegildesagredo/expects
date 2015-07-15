# -*- coding: utf-8 -*-

from expects import *
from expects.testing import failure


class Foo(object):
    bar = 0
    baz = 1


with describe('have_properties'):
    with before.each:
        self.obj = Foo()

    with it('passes if object has properties in args'):
        expect(self.obj).to(have_properties('bar', 'baz'))

    with it('passes if object has properties in kwargs'):
        expect(self.obj).to(have_properties(bar=0, baz=1))

    with it('passes if object has properties in args and kwargs'):
        expect(self.obj).to(have_properties('bar', baz=1))

    with it('passes if object has properties in dict'):
        expect(self.obj).to(have_properties({'bar': 0, 'baz': 1}))

    with it('passes if object has properties matching in kwargs'):
        expect(self.obj).to(have_properties(bar=be_an(int)))

    with it('fails if object does not have property in args'):
        with failure("but: property 'foo' not found"):
            expect(self.obj).to(have_properties('bar', 'foo'))

    with it('fails if object does not have property in kwargs'):
        with failure("but: property 'foo' not found"):
            expect(self.obj).to(have_properties(bar=0, foo=1))

    with it('fails if object has property without value in kwargs'):
        with failure("but: property 'bar' equal 1 not found"):
            expect(self.obj).to(have_properties(bar=1, baz=1))

    with it('fails if object does not have property in args but in kwargs'):
        with failure("but: property 'foo' not found"):
            expect(self.obj).to(have_properties('foo', bar=0))

    with it('fails if object has property in args and kwargs without value'):
        with failure("but: property 'bar' equal 1 not found"):
            expect(self.obj).to(have_properties('baz', bar=1))

    with it('fails if object has property without value in dict'):
        with failure("but: property 'bar' equal 1 not found"):
            expect(self.obj).to(have_properties({'bar': 1, 'baz': 1}))

    with it('fails if object has properties not matching in args'):
        with failure("but: property 'bar' be a str not found"):
            expect(self.obj).to(have_properties(bar=be_a(str)))

    with context('when negated'):
        with it('passes if object does not have properties in args'):
            expect(self.obj).to_not(have_properties('foo', 'foobar'))

        with it('passes if object does not have properties in kwargs'):
            expect(self.obj).not_to(have_properties(foo=0, foobar=1))

        with it('passes if object has property without value in kwargs'):
            expect(self.obj).not_to(have_properties(foo=0, bar=1))

        with it('passes if object does not have properties in dict'):
            expect(self.obj).not_to(have_properties({'foo': 0, 'foobar': 1}))

        with it('passes if object has property without value in dict'):
            expect(self.obj).not_to(have_properties({'foo': 0, 'bar': 1}))

        with it('passes if object has one property and not the other in args'):
            expect(self.obj).not_to(have_properties('foo', 'bar'))

        with it('fails if object has properties in args'):
            with failure("but: property 'bar' found\n          property 'baz' found"):
                expect(self.obj).to_not(have_properties('bar', 'baz'))

        with it('fails if object has properties in kwargs'):
            with failure(contain("property 'bar' equal 0 found") &
                         contain("property 'baz' equal 1 found")):

                expect(self.obj).not_to(have_properties(bar=0, baz=1))
