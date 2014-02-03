# -*- coding: utf-8 -*

from mamba import describe, context

from ..helpers import failure

from expects import expect


with describe('less_than'):
    def it_should_pass_if_actual_is_less_than_expected():
        expect(1).to.be.less_than(4)

    def it_should_fail_if_actual_is_not_less_than_expected():
        with failure(4, 'to be less than 1'):
            expect(4).to.be.less_than(1)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_less_than_expected():
            expect(4).not_to.be.less_than(1)

        def it_should_fail_if_actual_is_less_than_expected():
            with failure(1, 'not to be less than 4'):
                expect(1).not_to.be.less_than(4)
