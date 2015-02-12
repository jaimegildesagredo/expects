# -*- coding: utf-8 -*-

from specs.fixtures import Foo

from expects import *
from expects.testing import failure


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
        with failure("to have properties 'bar' and 'foo'"):
            expect(self.obj).to(have_properties('bar', 'foo'))

    with it('fails if object does not have property in kwargs'):
        with failure("to have properties 'bar' equal 0 and 'foo' equal 1"):
            expect(self.obj).to(have_properties(bar=0, foo=1))

    with it('fails if object has property without value in kwargs'):
        with failure("to have properties 'bar' equal 1 and 'baz' equal 1"):
            expect(self.obj).to(have_properties(bar=1, baz=1))

    with it('fails if object does not have property in args but in kwargs'):
        with failure("to have properties 'foo' and 'bar' equal 0"):
            expect(self.obj).to(have_properties('foo', bar=0))

    with it('fails if object has property in args and kwargs without value'):
        with failure("to have properties 'baz' and 'bar' equal 1"):
            expect(self.obj).to(have_properties('baz', bar=1))

    with it('fails if object has property without value in dict'):
        with failure("to have properties 'bar' equal 1 and 'baz' equal 1"):
            expect(self.obj).to(have_properties({'bar': 1, 'baz': 1}))

    with it('fails if object has properties not matching in args'):
        with failure("to have properties 'bar' be a str"):
            expect(self.obj).to(have_properties(bar=be_a(str)))

    with context('#negated'):
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
            with failure("not to have properties 'bar' and 'baz'"):
                expect(self.obj).to_not(have_properties('bar', 'baz'))

        with it('fails if object has properties in kwargs'):
            with failure("not to have properties 'bar' equal 0 and 'baz' equal 1"):
                expect(self.obj).not_to(have_properties(bar=0, baz=1))
