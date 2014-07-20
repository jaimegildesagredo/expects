# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('be_false'):
    def it_should_pass_if_object_is_false():
        expect(False).to(be_false)

    def it_should_fail_if_object_is_true():
        with failure('Expected True to be false'):
            expect(True).to(be_false)

    with context('#negated'):
        def it_should_pass_if_object_is_not_false():
            expect(True).not_to(be_false)

        def it_should_fail_if_object_is_false():
            with failure('Expected False not to be false'):
                expect(False).not_to(be_false)
