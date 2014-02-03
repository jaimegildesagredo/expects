# -*- coding: utf-8 -*

from mamba import describe, context

from ..helpers import failure

from expects import expect


with describe('greater_or_equal_to'):
    def it_should_pass_if_actual_is_greater_than_expected_():
        expect(5).to.be.greater_or_equal_to(4)

    def it_should_pass_if_actual_is_equal_to_expected():
        expect(5).to.be.greater_or_equal_to(5)

    def it_should_fail_if_actual_is_not_greater_or_equal_to_expected():
        with failure(1, 'to be greater or equal to 4'):
            expect(1).to.be.greater_or_equal_to(4)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_greater_or_equal_to_expected():
            expect(1).not_to.be.greater_or_equal_to(4)

        def it_should_fail_if_actual_is_greater_than_expected_():
            with failure(5, 'not to be greater or equal to 4'):
                expect(5).not_to.be.greater_or_equal_to(4)

        def it_should_fail_if_actual_is_equal_to_expected():
            with failure(5, 'not to be greater or equal to 5'):
                expect(5).not_to.be.greater_or_equal_to(5)
