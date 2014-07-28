# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import *
from expects.testing import failure


with describe('contain_exactly') as _:
    def it_should_pass_if_list_exactly_has_expected_item():
        expect(['bar']).to(contain_exactly('bar'))

    def it_should_pass_if_list_exactly_has_expected_items():
        expect(_.lst).to(contain_exactly(*_.lst))

    def it_should_pass_if_string_exactly_contains_string():
        expect(_.str).to(contain_exactly(_.str))

    def it_should_pass_if_string_exactly_contains_strings():
        expect(_.str).to(contain_exactly('My foo', ' string'))

    def it_should_fail_if_list_does_not_contain_expected_item_():
        with failure("to contain exactly 'foo'"):
            expect(_.lst).to(contain_exactly('foo'))

    def it_should_fail_if_list_does_not_contain_expected_items():
        with failure("to contain exactly 'foo' and 'fuu'"):
            expect(_.lst).to(contain_exactly('foo', 'fuu'))

    def it_should_fail_if_list_not_exactly_has_expected_item():
        with failure("to contain exactly 'bar'"):
            expect(_.lst).to(contain_exactly('bar'))

    def it_should_fail_if_list_not_exactly_has_two_expected_items():
        _.lst.append('foo')

        with failure("to contain exactly 'bar' and 'baz'"):
            expect(_.lst).to(contain_exactly('bar', 'baz'))

    def it_should_fail_if_list_not_exactly_has_three_expected_items():
        _.lst.extend(['foo', 'fuu'])

        with failure("to contain exactly 'bar', 'baz' and 'foo'"):
            expect(_.lst).to(contain_exactly('bar', 'baz', 'foo'))

    def it_should_fail_if_string_does_not_exactly_contain_string():
        with failure("to contain exactly 'foo'"):
            expect(_.str).to(contain_exactly('foo'))

    @before.each
    def fixtures():
        _.lst = ['bar', 'baz']
        _.itr = iter(_.lst)
        _.str = 'My foo string'
