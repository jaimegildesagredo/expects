# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('be_above'):
    def it_should_pass_if_number_is_above_expected():
        expect(5).to(be_above(4))

    def it_should_fail_if_number_is_not_above_expected():
        with failure('Expected 1 to be above 4'):
            expect(1).to(be_above(4))

    with context('#negated'):
        def it_should_pass_if_number_is_not_above_expected():
            expect(1).not_to(be_above(4))

        def it_should_fail_if_number_is_above_expected():
            with failure('Expected 5 not to be above 4'):
                expect(5).not_to(be_above(4))
