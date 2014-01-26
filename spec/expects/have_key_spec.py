# -*- coding: utf-8 -*

from mamba import describe, context, before

from spec.helpers import failure

from expects import expect


with describe('to.have.key') as _:
    def it_should_pass_if_actual_has_expected_key():
        expect(_.dct).to.have.key('bar')

    def it_should_pass_if_actual_has_key_and_value():
        expect(_.dct).to.have.key('bar', 0)

    def it_should_fail_if_actual_does_not_have_expected_key():
        with failure(_.dct, "to have key 'foo'"):
            expect(_.dct).to.have.key('foo')

    def it_should_fail_if_actual_does_not_have_key_with_value():
        with failure(_.dct, "to have key 'foo'"):
            expect(_.dct).to.have.key('foo', 0)

    def it_should_fail_if_actual_has_key_without_expected_value():
        with failure(_.dct, "to have key 'bar' with value 1 but was 0"):
            expect(_.dct).to.have.key('bar', 1)

    def it_should_fail_if_actual_has_key_without_none_value():
        with failure(_.dct, "to have key 'bar' with value None but was 0"):
            expect(_.dct).to.have.key('bar', None)

    def it_should_fail_if_actual_is_not_a_dict():
        # issue-10

        with failure(_.str, "to have key 'foo' but not a dict"):
            expect(_.str).to.have.key('foo', 0)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_expected_key():
            expect(_.dct).not_to.have.key('foo')

        def it_should_pass_if_actual_does_not_have_expected_key_with_value():
            expect(_.dct).not_to.have.key('foo', 0)

        def it_should_pass_if_actual_has_expected_key_without_value():
            expect(_.dct).not_to.have.key('bar', 1)

        def it_should_fail_if_actual_has_expected_key():
            with failure(_.dct, "not to have key 'bar'"):
                expect(_.dct).not_to.have.key('bar')

        def it_should_fail_if_actual_has_expected_key_with_value():
            with failure(_.dct, "not to have key 'bar' with value 0 but was 0"):
                expect(_.dct).not_to.have.key('bar', 0)

        def it_should_pass_if_actual_is_not_a_dict():
            # issue-10

            expect(_.str).not_to.have.key('foo', 0)

    with context('#chain'):
        def it_should_pass_if_actual_has_key_with_value_equal():
            expect(_.dct).to.have.key('bar').with_value.equal(0)

        def it_should_pass_if_actual_has_key_with_value_not_equal():
            expect(_.dct).to.have.key('bar').with_value.not_equal(1)

        def it_should_fail_if_actual_has_key_without_value_equal():
            with failure(_.dct, "to have key 'bar' with value 0 equal 1"):
                expect(_.dct).to.have.key('bar').with_value.equal(1)

        def it_should_fail_if_actual_has_key_without_value_not_equal():
            with failure(_.dct, "to have key 'bar' with value 0 not equal 0"):
                expect(_.dct).to.have.key('bar').with_value.not_equal(0)

    @before.all
    def fixtures():
        _.dct = {'bar': 0, 'baz': 1}
        _.str = 'My foo string'
