# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
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
        with failure("to have key 'foo'"):
            expect(_.dct).to(have_keys('bar', 'foo'))

    def it_should_fail_if_dict_does_not_have_key_in_kwargs():
        with failure("to have key 'foo' with value 1"):
            expect(_.dct).to(have_keys(bar=0, foo=1))

    def it_should_fail_if_dict_has_key_without_value_in_kwargs():
        with failure("to have key 'bar' with value 1"):
            expect(_.dct).to(have_keys(bar=1, baz=1))

    def it_should_fail_if_dict_does_not_have_key_in_args_but_in_kwargs():
        with failure("to have key 'foo'"):
            expect(_.dct).to(have_keys('foo', bar=0))

    def it_should_fail_if_dict_has_key_in_args_and_kwargs_without_value():
        with failure("to have key 'bar' with value 1"):
            expect(_.dct).to(have_keys('baz', bar=1))

    def it_should_fail_if_dict_has_key_without_value_in_dict():
        with failure("to have key 'bar' with value 1"):
            expect(_.dct).to(have_keys({'bar': 1, 'baz': 1}))

    with context('#negated'):
        def it_should_pass_if_dict_does_not_have_keys_in_args():
            expect(_.dct).not_to(have_keys('foo', 'foobar'))

        def it_should_pass_if_dict_does_not_have_keys_in_kwargs():
            expect(_.dct).not_to(have_keys(foo=0, foobar=1))

        def it_should_pass_if_dict_has_key_without_value_in_kwargs():
            expect(_.dct).not_to(have_keys(foo=0, bar=1))

        def it_should_pass_if_dict_does_not_have_keys_in_dict():
            expect(_.dct).not_to(have_keys({'foo': 0, 'foobar': 1}))

        def it_should_pass_if_dict_has_key_without_value_in_dict():
            expect(_.dct).not_to(have_keys({'foo': 0, 'bar': 1}))

        # TODO: Review these examples
        #def it_should_fail_if_dict_has_key_in_args():
            #with failure(''):
                #expect(_.dct).not_to(have_keys('foo', 'bar'))

        #def it_should_fail_if_dict_has_key_in_kwargs_with_value():
            #with failure(''):
                #expect(_.dct).not_to(have_keys(baz=0, bar=0))

        #def it_should_fail_if_dict_has_key_in_args_but_not_in_kwargs():
            #with failure(''):
                #expect(_.dct).not_to(have_keys('bar', baz=0))

        #def it_should_fail_if_dict_has_key_in_kwargs_but_not_in_args():
            #with failure(''):
                #expect(_.dct).not_to(have_keys('foo', bar=0))

            #def it_should_fail_if_dict_has_key_in_dict_with_value():
                #with failure(''):
                    #expect(_.dct).not_to(have_keys({'bar': 0, 'foo': 1}))

    @before.all
    def fixtures():
        _.dct = {'bar': 0, 'baz': 1}
