# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('contain'):
    with before.each:
        self.lst = ['bar', 'baz']
        self.itr = iter(self.lst)
        self.str = 'My foo string'

    with it('should pass if list contains item'):
        expect(self.lst).to(contain('bar'))

    with it('should pass if list contains items'):
        expect(self.lst).to(contain('bar', 'baz'))

    with it('should pass if iterable of dicts contains dict'):
        # https://github.com/jaimegildesagredo/expects/issues/8

        expect([{'foo': 1}, 'bar']).to(contain({'foo': 1}))

    with it('should pass if iterable contains item'):
        expect(self.itr).to(contain('bar'))

    with it('should pass if iterable contains items'):
        expect(self.itr).to(contain('bar', 'baz'))

    with it('should pass if string contains string'):
        expect(self.str).to(contain('foo'))

    with it('should pass if string contains strings'):
        expect(self.str).to(contain('foo', 'string'))

    with it('should fail if list does not contain item'):
        with failure("to contain 'bar' and 'foo'"):
            expect(self.lst).to(contain('bar', 'foo'))

    with it('should fail if iterable does not contain item'):
        with failure(end_with("to contain 'bar' and 'foo'")):
            expect(self.itr).to(contain('bar', 'foo'))

    with it('should fail if is not an iterable object'):
        with failure("to contain 'bar' but is not a valid sequence type"):
            expect(object()).to(contain('bar'))

    with context('#negated'):
        with it('should pass if list does not contain item'):
            expect(self.lst).not_to(contain('foo'))

        with it('should pass if list does not contain items'):
            expect(self.lst).not_to(contain('foo', 'foobar'))

        with it('should pass if list contains one item and not the other'):
            expect(self.lst).not_to(contain('bar', 'foo'))

        with it('should fail if list contains item'):
            with failure("not to contain 'bar'"):
                expect(self.lst).not_to(contain('bar'))

        with it('should fail if list contains items'):
            with failure("not to contain 'bar' and 'baz'"):
                expect(self.lst).not_to(contain('bar', 'baz'))

        with it('should fail if is not an iterable object'):
            with failure("not to contain 'bar' but is not a valid sequence type"):
                expect(object()).not_to(contain('bar'))
