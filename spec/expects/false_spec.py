# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('false'):
    def it_should_pass_if_actual_is_false():
        expect(False).to.be.false

    def it_should_fail_if_actual_is_true():
        with failure(True, 'to be False'):
            expect(True).to.be.false

    with context('#negated'):
        def it_should_pass_if_actual_is_not_false():
            expect(True).not_to.be.false

        def it_should_fail_if_actual_is_false_():
            with failure(False, 'not to be False'):
                expect(False).not_to.be.false
