# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('below'):
    def it_should_pass_if_actual_is_below_expected():
        expect(1).to.be.below(4)

    def it_should_fail_if_actual_is_not_below_expected():
        with failure(4, 'to be below 1'):
            expect(4).to.be.below(1)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_below_expected():
            expect(4).not_to.be.below(1)

        def it_should_fail_if_actual_is_below_expected():
            with failure(1, 'not to be below 4'):
                expect(1).not_to.be.below(4)
