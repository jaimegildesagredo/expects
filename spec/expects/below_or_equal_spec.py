# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('be_below_or_equal'):
    def it_should_pass_if_number_is_below_expected():
        expect(1).to(be_below_or_equal(4))

    def it_should_pass_if_number_is_equals_expected():
        expect(5).to(be_below_or_equal(5))

    def it_should_fail_if_number_is_not_below_or_equal_expected():
        with failure('Expected 4 to be below or equal 1'):
            expect(4).to(be_below_or_equal(1))

    with context('#negated'):
        def it_should_pass_if_number_is_not_below_or_equal_expected():
            expect(4).not_to(be_below_or_equal(1))

        def it_should_fail_if_number_is_below_expected():
            with failure('Expected 1 not to be below or equal 4'):
                expect(1).not_to(be_below_or_equal(4))

        def it_should_fail_if_number_equals_expected():
            with failure('Expected 5 not to be below or equal 5'):
                expect(5).not_to(be_below_or_equal(5))
