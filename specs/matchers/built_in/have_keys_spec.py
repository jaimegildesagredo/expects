# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('have_keys'):
    with before.each:
        self.dct = {'bar': 0, 'baz': 1}
        self.str = 'My foo string'

    with it('should_pass_if_dict_has_keys_in_args'):
        expect(self.dct).to(have_keys('bar', 'baz'))

    with it('should_pass_if_dict_has_keys_in_kwargs'):
        expect(self.dct).to(have_keys(bar=0, baz=1))

    with it('should_pass_if_dict_has_keys_in_args_and_kwargs'):
        expect(self.dct).to(have_keys('bar', baz=1))

    with it('should_pass_if_dict_has_keys_in_dict'):
        expect(self.dct).to(have_keys({'bar': 0, 'baz': 1}))

    with it('should_fail_if_dict_does_not_have_key_in_args'):
        with failure("to have keys 'bar' and 'foo'"):
            expect(self.dct).to(have_keys('bar', 'foo'))

    with it('should_fail_if_dict_does_not_have_key_in_kwargs'):
        with failure("to have keys 'bar' equal 0 and 'foo' equal 1"):
            expect(self.dct).to(have_keys(bar=0, foo=1))

    with it('should_fail_if_dict_has_key_without_value_in_kwargs'):
        with failure("to have keys 'bar' equal 1 and 'baz' equal 1"):
            expect(self.dct).to(have_keys(bar=1, baz=1))

    with it('should_fail_if_dict_does_not_have_key_in_args_but_in_kwargs'):
        with failure("to have keys 'foo', 'fuu' and 'bar' equal 0"):
            expect(self.dct).to(have_keys('foo', 'fuu', bar=0))

    with it('should_fail_if_dict_has_key_in_args_and_kwargs_without_value'):
        with failure("to have keys 'baz' and 'bar' equal 1"):
            expect(self.dct).to(have_keys('baz', bar=1))

    with it('should_fail_if_dict_has_key_without_value_in_dict'):
        with failure("to have keys 'bar' equal 1 and 'baz' equal 1"):
            expect(self.dct).to(have_keys({'bar': 1, 'baz': 1}))

    with it('should_fail_if_actual_is_not_a_dict'):
        # issue-10

        with failure("to have keys 'bar' equal 1 and 'baz' equal 1 but is not a dict"):
            expect(self.str).to(have_keys({'bar': 1, 'baz': 1}))

    with context('#negated'):
        with it('should_pass_if_dict_does_not_have_keys_in_args'):
            expect(self.dct).not_to(have_keys('foo', 'foobar'))

        with it('should_pass_if_dict_does_not_have_keys_in_kwargs'):
            expect(self.dct).not_to(have_keys(foo=0, foobar=1))

        with it('should_pass_if_dict_has_key_without_value_in_kwargs'):
            expect(self.dct).to_not(have_keys(foo=0, bar=1))

        with it('should_pass_if_dict_does_not_have_keys_in_dict'):
            expect(self.dct).to_not(have_keys({'foo': 0, 'foobar': 1}))

        with it('should_pass_if_dict_has_one_key_and_not_the_other_in_args'):
            expect(self.dct).not_to(have_keys('foo', 'bar'))

        with it('should_fail_if_dict_has_keys_in_args'):
            with failure("not to have keys 'bar' and 'baz'"):
                expect(self.dct).to_not(have_keys('bar', 'baz'))

        with it('should_fail_if_dict_has_keys_in_kwargs'):
            with failure("not to have keys 'bar' equal 0 and 'baz' equal 1"):
                expect(self.dct).not_to(have_keys(bar=0, baz=1))

        with it('should_fail_if_actual_is_not_a_dict'):
            # issue-10

            with failure("not to have keys 'bar' equal 1 and 'baz' equal 1 but is not a dict"):
                expect(self.str).not_to(have_keys({'bar': 1, 'baz': 1}))
