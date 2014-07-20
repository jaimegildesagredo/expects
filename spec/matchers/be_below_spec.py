# -*- coding: utf-8 -*

from mamba import describe, context

from expects import *
from expects.testing import failure


with describe('be_below'):
    def it_should_pass_if_number_is_below_expected():
        expect(1).to(be_below(4))

    def it_should_fail_if_number_is_not_below_expected():
        with failure('Expected 4 to be below 1'):
            expect(4).to(be_below(1))

    with context('#negated'):
        def it_should_pass_if_number_is_not_below_expected():
            expect(4).not_to(be_below(1))

        def it_should_fail_if_number_is_below_expected():
            with failure('Expected 1 not to be below 4'):
                expect(1).not_to(be_below(4))
