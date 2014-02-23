# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('none'):
    def it_should_pass_if_actual_is_none():
        expect(None).to.be.none

    def it_should_fail_if_actual_is_not_none():
        with failure(True, 'to be None'):
            expect(True).to.be.none

    with context('#negated'):
        def it_should_pass_if_actual_is_not_none():
            expect('foo').not_to.be.none

        def it_should_fail_if_actual_is_none():
            with failure(None, 'not to be None'):
                expect(None).not_to.be.none
