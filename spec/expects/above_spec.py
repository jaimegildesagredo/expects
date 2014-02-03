# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('above'):
    def it_should_pass_if_actual_is_above_expected():
        expect(5).to.be.above(4)

    def it_should_fail_if_actual_is_not_above_expected():
        with failure(1, 'to be above 4'):
            expect(1).to.be.above(4)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_above_expected():
            expect(1).not_to.be.above(4)

        def it_should_fail_if_actual_is_above_expected():
            with failure(5, 'not to be above 4'):
                expect(5).not_to.be.above(4)
