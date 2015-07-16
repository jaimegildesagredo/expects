# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('contain_only'):
    with before.each:
        self.lst = ['bar', 'baz']
        self.itr = iter(self.lst)
        self.str = 'My foo string'

    with it('passes if list only has expected item'):
        expect(['bar']).to(contain_only('bar'))

    with it('passes if list only has expected items'):
        expect(self.lst).to(contain_only(*self.lst))

    with it('passes if list only has expected items in any order'):
        expect(self.lst).to(contain_only(*reversed(self.lst)))

    with it('passes if iterable only has items'):
        expect(self.itr).to(contain_only('bar', 'baz'))

    with it('passes if string only contains string'):
        expect(self.str).to(contain_only(self.str))

    with it('passes if string only contains strings'):
        expect(self.str).to(contain_only('My foo', ' string'))

    with it('passes if list only has expected matching items'):
        expect(self.lst).to(contain_only(equal('bar'), equal('baz')))

    with it('fails if list does not have item'):
        with failure("but: item equal 'foo' not found"):
            expect(self.lst).to(contain_only('foo'))

    with it('fails if list has two expected items but has a different length'):
        self.lst.append('foo')

        with failure("but: have a different length"):
            expect(self.lst).to(contain_only('bar', 'baz'))

    with it('fails if string contains string and more'):
        with failure("but: have a different length"):
            expect(self.str).to(contain_only('foo'))

    with it('fails if string does not contain item'):
        with failure("but: item 'bar' not found"):
            expect(self.str).to(contain_only('bar'))

    with it('fails if is not an iterable object'):
        with failure("but: is not a valid sequence type"):
            expect(object()).to(contain_only('bar'))

    with it('fails if list does not have matching items'):
        with failure(''):
            expect(self.lst).to(contain_only(equal('baz'), equal('foo')))
