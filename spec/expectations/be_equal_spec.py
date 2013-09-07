# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('to.be.equal'):
    def it_should_pass_if_actual_equals_expected_():
        expect(1).to.be.equal(1)

    def it_should_fail_if_actual_does_not_equal_expected_():
        with failure(1, 'to be equal 2'):
            expect(1).to.be.equal(2)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_equal_expected_():
            expect(1).not_to.be.equal(2)

        def it_should_fail_if_actual_equals_expected_():
            with failure(1, 'not to be equal 1'):
                expect(1).not_to.be.equal(1)
