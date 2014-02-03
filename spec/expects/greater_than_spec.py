# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('greater_than'):
    def it_should_pass_if_actual_is_greater_than_expected():
        expect(5).to.be.greater_than(4)

    def it_should_fail_if_actual_is_not_greater_than_expected():
        with failure(1, 'to be greater than 4'):
            expect(1).to.be.greater_than(4)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_greater_than_expected():
            expect(1).not_to.be.greater_than(4)

        def it_should_fail_if_actual_is_greater_than_expected():
            with failure(5, 'not to be greater than 4'):
                expect(5).not_to.be.greater_than(4)
