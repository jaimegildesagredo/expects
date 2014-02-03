# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('within'):
    def it_should_pass_if_actual_is_within_expected_range():
        expect(5).to.be.within(4, 7)

    def it_should_fail_if_actual_is_not_within_expected_range():
        with failure(1, 'to be within 4, 7'):
            expect(1).to.be.within(4, 7)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_within_expected_range():
            expect(1).not_to.be.within(4, 7)

        def it_should_fail_if_actual_is_within_expected_range():
            with failure(5, 'not to be within 4, 7'):
                expect(5).not_to.be.within(4, 7)
