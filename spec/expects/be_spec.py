# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('be'):
    def it_should_pass_if_object_is_expected():
        value = 1
        expect(value).to(be(value))

    def it_should_fail_if_object_is_not_expected():
        with failure('Expected 1 to be 2'):
            expect(1).to(be(2))

    with context('#negated'):
        def it_should_pass_if_object_is_not_expected():
            expect(1).not_to(be(2))

        def it_should_fail_if_object_is_expected():
            value = 1

            with failure('Expected 1 not to be 1'):
                expect(value).not_to(be(value))
