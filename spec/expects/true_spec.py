# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('be_true'):
    def it_should_pass_if_object_is_true():
        expect(True).to(be_true)

    def it_should_fail_if_object_is_false():
        with failure(''):
            expect(False).to(be_true)

    with context('#negated'):
        def it_should_pass_if_object_is_not_true():
            expect(False).not_to(be_true)

        def it_should_fail_if_object_is_true():
            with failure(''):
                expect(True).not_to(be_true)
