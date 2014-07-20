# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('be_above_or_equal'):
    def it_should_pass_if_number_is_above_expected():
        expect(5).to(be_above_or_equal(4))

    def it_should_pass_if_number_equals_expected():
        expect(5).to(be_above_or_equal(5))

    def it_should_fail_if_number_is_not_above_or_equal_expected():
        with failure('Expected 1 to be above or equal 4'):
            expect(1).to(be_above_or_equal(4))

    with context('#negated'):
        def it_should_pass_if_number_is_not_above_or_equal_expected():
            expect(1).not_to(be_above_or_equal(4))

        def it_should_fail_if_number_is_above_expected():
            with failure('Expected 5 not to be above or equal 4'):
                expect(5).not_to(be_above_or_equal(4))

        def it_should_fail_if_number_equals_expected():
            with failure('Expected 5 not to be above or equal 5'):
                expect(5).not_to(be_above_or_equal(5))
