# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('contain_only') as _:
    def it_should_pass_if_list_only_has_expected_item():
        expect(['bar']).to(contain_only('bar'))

    def it_should_pass_if_list_only_has_expected_items():
        expect(_.lst).to(contain_only(*_.lst))

    def it_should_pass_if_string_only_contains_string():
        expect(_.str).to(contain_only(_.str))

    def it_should_pass_if_string_only_contains_strings():
        expect(_.str).to(contain_only('My foo', ' string'))

    def it_should_fail_if_list_does_not_contain_expected_item_():
        with failure("to contain only 'foo'"):
            expect(_.lst).to(contain_only('foo'))

    def it_should_fail_if_list_does_not_contain_expected_items():
        with failure("to contain only 'foo' and 'fuu'"):
            expect(_.lst).to(contain_only('foo', 'fuu'))

    def it_should_fail_if_list_not_only_has_expected_item():
        with failure("to contain only 'bar'"):
            expect(_.lst).to(contain_only('bar'))

    def it_should_fail_if_list_not_only_has_two_expected_items():
        _.lst.append('foo')

        with failure("to contain only 'bar' and 'baz'"):
            expect(_.lst).to(contain_only('bar', 'baz'))

    def it_should_fail_if_list_not_only_has_three_expected_items():
        _.lst.extend(['foo', 'fuu'])

        with failure("to contain only 'bar', 'baz' and 'foo'"):
            expect(_.lst).to(contain_only('bar', 'baz', 'foo'))

    def it_should_fail_if_string_does_not_only_contain_string():
        with failure("to contain only 'foo'"):
            expect(_.str).to(contain_only('foo'))

    @before.each
    def fixtures():
        _.lst = ['bar', 'baz']
        _.itr = iter(_.lst)
        _.str = 'My foo string'
