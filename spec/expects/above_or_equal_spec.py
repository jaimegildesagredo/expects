# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('above_or_equal'):
    def it_should_pass_if_number_is_above_expected():
        expect(5).to.be(above_or_equal(4))

    def it_should_pass_if_number_equals_expected():
        expect(5).to.be(above_or_equal(5))

    def it_should_fail_if_number_is_not_above_or_equal_expected():
        with failure(''):
            expect(1).to.be(above_or_equal(4))

    with context('#negated'):
        def it_should_pass_if_number_is_not_above_or_equal_expected():
            expect(1).not_to.be(above_or_equal(4))

        def it_should_fail_if_number_is_above_expected():
            with failure(''):
                expect(5).not_to.be(above_or_equal(4))

        def it_should_fail_if_number_equals_expected():
            with failure(''):
                expect(5).not_to.be(above_or_equal(5))
