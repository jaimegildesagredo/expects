# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('contain') as _:
    def it_should_pass_if_list_has_expected_item():
        expect(_.lst).to(contain('bar'))

    def it_should_pass_if_list_has_expected_items():
        expect(_.lst).to(contain('bar', 'baz'))

    def it_should_pass_if_iterable_of_dicts_has_dict():
        # https://github.com/jaimegildesagredo/expects/issues/8

        expect([{'foo': 1}, 'bar']).to(contain({'foo': 1}))

    def it_should_pass_if_iterable_has_expected_item():
        expect(_.itr).to(contain('bar'))

    def it_should_pass_if_iterable_has_expected_items():
        expect(_.itr).to(contain('bar', 'baz'))

    def it_should_fail_if_list_does_not_contain_expected_item():
        with failure(''):
            expect(_.lst).to(contain('bar', 'foo'))

    def it_should_fail_if_iterable_does_not_contain_expected_item():
        with failure(''):
            expect(_.itr).to(contain('bar', 'foo'))

    def it_should_pass_if_string_contains_string():
        expect(_.str).to(contain('foo'))

    def it_should_pass_if_string_contains_strings():
        expect(_.str).to(contain('foo', 'string'))

    with context('#negated'):
        def it_should_pass_if_list_does_not_contain_expected_item():
            expect(_.lst).not_to(contain('foo'))

        def it_should_pass_if_list_does_not_contain_expected_items():
            expect(_.lst).not_to(contain('foo', 'foobar'))

        # TODO: Review this example
        #def it_should_fail_if_list_has_expected_item():
            #with failure(''):
                #expect(_.lst).not_to(contain('bar', 'foo'))

    @before.each
    def fixtures():
        _.lst = ['bar', 'baz']
        _.itr = iter(_.lst)
        _.str = 'My foo string'
