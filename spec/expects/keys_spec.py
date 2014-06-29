# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('keys') as _:
    def it_should_pass_if_actual_has_keys_in_args():
        expect(_.dct).to.have.keys('bar', 'baz')

    def it_should_pass_if_actual_has_keys_in_kwargs():
        expect(_.dct).to.have.keys(bar=0, baz=1)

    def it_should_pass_if_actual_has_keys_in_args_and_kwargs():
        expect(_.dct).to.have.keys('bar', baz=1)

    def it_should_pass_if_actual_has_keys_in_dict():
        expect(_.dct).to.have.keys({'bar': 0, 'baz': 1})

    def it_should_fail_if_actual_does_not_have_key_in_args():
        with failure(_.dct, "to have key 'foo'"):
            expect(_.dct).to.have.keys('bar', 'foo')

    def it_should_fail_if_actual_does_not_have_key_in_kwargs():
        with failure(_.dct, "to have key 'foo'"):
            expect(_.dct).to.have.keys(bar=0, foo=1)

    def it_should_fail_if_actual_has_key_without_value_in_kwargs():
        with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
            expect(_.dct).to.have.keys(bar=1, baz=1)

    def it_should_fail_if_actual_does_not_have_key_in_args_but_in_kwargs():
        with failure(_.dct, "to have key 'foo'"):
            expect(_.dct).to.have.keys('foo', bar=0)

    def it_should_fail_if_actual_has_key_in_args_and_kwargs_without_value():
        with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
            expect(_.dct).to.have.keys('baz', bar=1)

    def it_should_fail_if_actual_has_key_without_value_in_dict():
        with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
            expect(_.dct).to.have.keys({'bar': 1, 'baz': 1})

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_keys_in_args():
            expect(_.dct).not_to.have.keys('foo', 'foobar')

        def it_should_pass_if_actual_does_not_have_keys_in_kwargs():
            expect(_.dct).not_to.have.keys(foo=0, foobar=1)

        def it_should_pass_if_actual_has_key_without_value_in_kwargs():
            expect(_.dct).not_to.have.keys(foo=0, bar=1)

        def it_should_pass_if_actual_does_not_have_keys_in_dict():
            expect(_.dct).not_to.have.keys({'foo': 0, 'foobar': 1})

        def it_should_pass_if_actual_has_key_without_value_in_dict():
            expect(_.dct).not_to.have.keys({'foo': 0, 'bar': 1})

        def it_should_fail_if_actual_has_key_in_args():
            with failure(_.dct, "not to have key 'bar'"):
                expect(_.dct).not_to.have.keys('foo', 'bar')

        def it_should_fail_if_actual_has_key_in_kwargs_with_value():
            with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                expect(_.dct).not_to.have.keys(baz=0, bar=0)

        def it_should_fail_if_actual_has_key_in_args_but_not_in_kwargs():
            with failure(_.dct, "not to have key 'bar'"):
                expect(_.dct).not_to.have.keys('bar', baz=0)

        def it_should_fail_if_actual_has_key_in_kwargs_but_not_in_args():
            with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                expect(_.dct).not_to.have.keys('foo', bar=0)

            def it_should_fail_if_actual_has_key_in_dict_with_value():
                with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                    expect(_.dct).not_to.have.keys({'bar': 0, 'foo': 1})

    with describe('only'):
        def it_should_pass_if_dict_has_keys():
            expect(_.dct).to.only.have.keys('bar', 'baz')

        def it_should_pass_if_dict_has_keys_with_values():
            expect(_.dct).to.only.have.keys(bar=0, baz=1)

        def it_should_fail_if_dict_does_not_have_keys():
            with failure(_.dct, "to only have key 'foo'"):
                expect(_.dct).to.only.have.keys('foo', 'fuu')

        def it_should_fail_if_dict_does_not_only_have_keys():
            _.dct['foo'] = 2

            with failure(_.dct, "to only have keys 'bar' and 'baz'"):
                expect(_.dct).to.only.have.keys('bar', 'baz')

        def it_should_fail_if_dict_does_not_only_have_keys_with_values():
            _.dct['foo'] = 2

            with failure(_.dct, "to only have keys 'bar' with value 0 and 'baz' with value 1"):
                expect(_.dct).to.only.have.keys(bar=0, baz=1)

    @before.each
    def fixtures():
        _.dct = {'bar': 0, 'baz': 1}
