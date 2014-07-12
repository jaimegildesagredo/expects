# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('have') as _:
    def it_should_pass_if_list_has_expected_item():
        expect(_.lst).to(have('bar'))

    def it_should_pass_if_list_has_expected_items():
        expect(_.lst).to(have('bar', 'baz'))

    def it_should_pass_if_iterable_of_dicts_has_dict():
        # https://github.com/jaimegildesagredo/expects/issues/8

        expect([{'foo': 1}, 'bar']).to(have({'foo': 1}))

    def it_should_pass_if_iterable_has_expected_item():
        expect(_.itr).to(have('bar'))

    def it_should_pass_if_iterable_has_expected_items():
        expect(_.itr).to(have('bar', 'baz'))

    def it_should_fail_if_list_does_not_have_expected_item():
        with failure(''):
            expect(_.lst).to(have('bar', 'foo'))

    def it_should_fail_if_iterable_does_not_have_expected_item():
        with failure(''):
            expect(_.itr).to(have('bar', 'foo'))

    def it_should_pass_if_string_contains_string():
        expect(_.str).to(have('foo'))

    def it_should_pass_if_string_contains_strings():
        expect(_.str).to(have('foo', 'string'))

    with context('#negated'):
        def it_should_pass_if_list_does_not_have_expected_item():
            expect(_.lst).not_to(have('foo'))

        def it_should_pass_if_list_does_not_have_expected_items():
            expect(_.lst).not_to(have('foo', 'foobar'))

        # TODO: Review this example
        #def it_should_fail_if_list_has_expected_item():
            #with failure(''):
                #expect(_.lst).not_to(have('bar', 'foo'))

    with describe('only'):
        def it_should_pass_if_list_only_has_expected_item():
            expect(['bar']).to(have.only('bar'))

        def it_should_pass_if_list_only_has_expected_items():
            expect(_.lst).to(have.only(*_.lst))

        def it_should_pass_if_string_only_contains_string():
            expect(_.str).to(have.only(_.str))

        def it_should_pass_if_string_only_contains_strings():
            expect(_.str).to(have.only('My foo', ' string'))

        def it_should_fail_if_list_does_not_have_expected_item_():
            with failure(''):
                expect(_.lst).to(have.only('foo'))

        def it_should_fail_if_list_does_not_have_expected_items():
            with failure(''):
                expect(_.lst).to(have.only('foo', 'fuu'))

        def it_should_fail_if_list_not_only_has_expected_item():
            with failure(''):
                expect(_.lst).to(have.only('bar'))

        def it_should_fail_if_list_not_only_has_two_expected_items():
            _.lst.append('foo')

            with failure(''):
                expect(_.lst).to(have.only('bar', 'baz'))

        def it_should_fail_if_list_not_only_has_three_expected_items():
            _.lst.extend(['foo', 'fuu'])

            with failure(''):
                expect(_.lst).to(have.only('bar', 'baz', 'foo'))

        def it_should_fail_if_string_does_not_only_contain_string():
            with failure(''):
                expect(_.str).to(have.only('foo'))

    @before.each
    def fixtures():
        _.lst = ['bar', 'baz']
        _.itr = iter(_.lst)
        _.str = 'My foo string'
