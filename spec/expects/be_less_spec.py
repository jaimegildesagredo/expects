# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('to.be'):
    with describe('less_than'):
        def it_should_pass_if_actual_is_less_than_expected():
            expect(1).to.be.less_than(4)

        def it_should_fail_if_actual_is_not_less_than_expected():
            with failure(4, 'to be less than 1'):
                expect(4).to.be.less_than(1)

    with describe('less_or_equal_to'):
        def it_should_pass_if_actual_is_less_than_expected_():
            expect(1).to.be.less_or_equal_to(4)

        def it_should_pass_if_actual_is_equal_to_expected_():
            expect(5).to.be.less_or_equal_to(5)

        def it_should_fail_if_actual_is_not_less_or_equal_to_expected():
            with failure(4, 'to be less or equal to 1'):
                expect(4).to.be.less_or_equal_to(1)

    with context('#negated'):
        with describe('less_than'):
            def it_should_pass_if_actual_is_not_less_than_expected():
                expect(4).not_to.be.less_than(1)

            def it_should_fail_if_actual_is_less_than_expected():
                with failure(1, 'not to be less than 4'):
                    expect(1).not_to.be.less_than(4)

        with describe('less_or_equal_to'):
            def it_should_pass_if_actual_is_not_less_or_equal_to_expected():
                expect(4).not_to.be.less_or_equal_to(1)

            def it_should_fail_if_actual_is_less_than_expected_():
                with failure(1, 'not to be less or equal to 4'):
                    expect(1).not_to.be.less_or_equal_to(4)

            def it_should_fail_if_actual_is_equal_to_expected_():
                with failure(5, 'not to be less or equal to 5'):
                    expect(5).not_to.be.less_or_equal_to(5)
