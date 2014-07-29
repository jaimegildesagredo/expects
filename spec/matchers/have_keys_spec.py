# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import *
from expects.testing import failure


with describe('have_keys') as _:
    def it_should_pass_if_dict_has_keys_in_args():
        expect(_.dct).to(have_keys('bar', 'baz'))

    def it_should_pass_if_dict_has_keys_in_kwargs():
        expect(_.dct).to(have_keys(bar=0, baz=1))

    def it_should_pass_if_dict_has_keys_in_args_and_kwargs():
        expect(_.dct).to(have_keys('bar', baz=1))

    def it_should_pass_if_dict_has_keys_in_dict():
        expect(_.dct).to(have_keys({'bar': 0, 'baz': 1}))

    def it_should_fail_if_dict_does_not_have_key_in_args():
        with failure("to have keys 'bar' and 'foo'"):
            expect(_.dct).to(have_keys('bar', 'foo'))

    def it_should_fail_if_dict_does_not_have_key_in_kwargs():
        with failure("to have keys bar=0 and foo=1"):
            expect(_.dct).to(have_keys(bar=0, foo=1))

    def it_should_fail_if_dict_has_key_without_value_in_kwargs():
        with failure("to have keys bar=1 and baz=1"):
            expect(_.dct).to(have_keys(bar=1, baz=1))

    def it_should_fail_if_dict_does_not_have_key_in_args_but_in_kwargs():
        with failure("to have keys 'foo', 'fuu' and bar=0"):
            expect(_.dct).to(have_keys('foo', 'fuu', bar=0))

    def it_should_fail_if_dict_has_key_in_args_and_kwargs_without_value():
        with failure("to have keys 'baz' and bar=1"):
            expect(_.dct).to(have_keys('baz', bar=1))

    def it_should_fail_if_dict_has_key_without_value_in_dict():
        with failure("to have keys bar=1 and baz=1"):
            expect(_.dct).to(have_keys({'bar': 1, 'baz': 1}))

    def it_should_fail_if_actual_is_not_a_dict():
        # issue-10

        with failure("to have keys bar=1 and baz=1 but is not a dict"):
            expect(_.str).to(have_keys({'bar': 1, 'baz': 1}))

    with context('#negated'):
        def it_should_pass_if_dict_does_not_have_keys_in_args():
            expect(_.dct).not_to(have_keys('foo', 'foobar'))

        def it_should_pass_if_dict_does_not_have_keys_in_kwargs():
            expect(_.dct).not_to(have_keys(foo=0, foobar=1))

        def it_should_pass_if_dict_has_key_without_value_in_kwargs():
            expect(_.dct).not_to(have_keys(foo=0, bar=1))

        def it_should_pass_if_dict_does_not_have_keys_in_dict():
            expect(_.dct).not_to(have_keys({'foo': 0, 'foobar': 1}))

        def it_should_pass_if_dict_has_one_key_and_not_the_other_in_args():
            expect(_.dct).not_to(have_keys('foo', 'bar'))

        def it_should_fail_if_dict_has_keys_in_args():
            with failure("not to have keys 'bar' and 'baz'"):
                expect(_.dct).not_to(have_keys('bar', 'baz'))

        def it_should_fail_if_dict_has_keys_in_kwargs():
            with failure("not to have keys bar=0 and baz=1"):
                expect(_.dct).not_to(have_keys(bar=0, baz=1))

        def it_should_fail_if_actual_is_not_a_dict_():
            # issue-10

            with failure("not to have keys bar=1 and baz=1 but is not a dict"):
                expect(_.str).not_to(have_keys({'bar': 1, 'baz': 1}))

    @before.all
    def fixtures():
        _.dct = {'bar': 0, 'baz': 1}
        _.str = 'My foo string'
