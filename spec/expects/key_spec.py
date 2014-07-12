# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure


with describe('key') as _:
    def it_should_pass_if_actual_has_expected_key():
        expect(_.dct).to.have(key('bar'))

    def it_should_pass_if_actual_has_key_and_value():
        expect(_.dct).to.have(key('bar', 0))

    def it_should_fail_if_actual_does_not_have_expected_key():
        with failure(''):
            expect(_.dct).to.have(key('foo'))

    def it_should_fail_if_actual_does_not_have_key_with_value():
        with failure(''):
            expect(_.dct).to.have(key('foo', 0))

    def it_should_fail_if_actual_has_key_without_expected_value():
        with failure(''):
            expect(_.dct).to.have(key('bar', 1))

    def it_should_fail_if_actual_has_key_without_none_value():
        with failure(''):
            expect(_.dct).to.have(key('bar', None))

    def it_should_fail_if_actual_is_not_a_dict():
        # issue-10

        with failure(''):
            expect(_.str).to.have(key('foo', 0))

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_expected_key():
            expect(_.dct).not_to.have(key('foo'))

        def it_should_pass_if_actual_does_not_have_expected_key_with_value():
            expect(_.dct).not_to.have(key('foo', 0))

        def it_should_pass_if_actual_has_expected_key_without_value():
            expect(_.dct).not_to.have(key('bar', 1))

        def it_should_fail_if_actual_has_expected_key():
            with failure(''):
                expect(_.dct).not_to.have(key('bar'))

        def it_should_fail_if_actual_has_expected_key_with_value():
            with failure(''):
                expect(_.dct).not_to.have(key('bar', 0))

        def it_should_pass_if_actual_is_not_a_dict():
            # issue-10

            expect(_.str).not_to.have(key('foo', 0))

    with context('#composed'):
        def it_should_pass_if_actual_has_key_with_value_equal():
            expect(_.dct).to.have(key('bar', equal(0)))

        def it_should_fail_if_actual_has_key_without_value_equal():
            with failure(''):
                expect(_.dct).to.have(key('bar', equal(1)))

    @before.all
    def fixtures():
        _.dct = {'bar': 0, 'baz': 1}
        _.str = 'My foo string'
