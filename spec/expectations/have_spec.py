# -*- coding: utf-8 -*

from mamba import describe, context, before

from spec.helpers import failure

from expects import expect


with describe('have') as _:
    def it_should_pass_if_actual_has_expected_item():
        expect(_.lst).to.have('bar')

    def it_should_pass_if_actual_has_expected_items():
        expect(_.lst).to.have('bar', 'baz')

    def it_should_fail_if_actual_does_not_have_expected_item():
        with failure(_.lst, "to have 'foo'"):
            expect(_.lst).to.have('bar', 'foo')

    def it_should_pass_if_actual_iterable_has_expected_item():
        expect(_.itr).to.have('bar')

    def it_should_pass_if_actual_iterable_has_expected_items():
        expect(_.itr).to.have('bar', 'baz')

    def it_should_fail_if_actual_iterable_does_not_have_expected_item():
        with failure(_.itr, "to have 'foo'"):
            expect(_.itr).to.have('bar', 'foo')

    def it_should_pass_if_iterable_of_dicts_has_dict():
        # issue-8

        expect([{'foo': 1}, 'bar']).to.have({'foo': 1})

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_expected_item():
            expect(_.lst).not_to.have('foo')

        def it_should_pass_if_actual_does_not_have_expected_items():
            expect(_.lst).not_to.have('foo', 'foobar')

        def it_should_fail_if_actual_has_expected_item():
            with failure(_.lst, "not to have 'bar'"):
                expect(_.lst).not_to.have('bar', 'foo')

    @before.each
    def fixtures():
        _.lst = ['bar', 'baz']
        _.itr = iter(_.lst)
