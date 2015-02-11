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

    with it('fails if list does not contain expected item'):
        with failure("to contain only 'foo'"):
            expect(self.lst).to(contain_only('foo'))

    with it('fails if list not only has two expected items'):
        self.lst.append('foo')

        with failure("to contain only 'bar' and 'baz'"):
            expect(self.lst).to(contain_only('bar', 'baz'))

    with it('fails if string does not only contain string'):
        with failure("to contain only 'foo'"):
            expect(self.str).to(contain_only('foo'))

    with it('fails if is not an iterable object'):
        with failure("to contain only 'bar' but is not a valid sequence type"):
            expect(object()).to(contain_only('bar'))

    with it('fails if list does not contain only matching items'):
        with failure:
            expect(self.lst).to(contain_only(equal('baz'), equal('foo')))
