# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('above_or_equal'):
    def it_should_pass_if_actual_is_above_expected():
        expect(5).to.be.above_or_equal(4)

    def it_should_pass_if_actual_equals_expected():
        expect(5).to.be.above_or_equal(5)

    def it_should_fail_if_actual_is_not_above_or_equal_expected():
        with failure(1, 'to be above or equal 4'):
            expect(1).to.be.above_or_equal(4)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_above_or_equal_expected():
            expect(1).not_to.be.above_or_equal(4)

        def it_should_fail_if_actual_is_above_expected():
            with failure(5, 'not to be above or equal 4'):
                expect(5).not_to.be.above_or_equal(4)

        def it_should_fail_if_actual_equals_expected():
            with failure(5, 'not to be above or equal 5'):
                expect(5).not_to.be.above_or_equal(5)
