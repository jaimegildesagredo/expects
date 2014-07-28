# -*- coding: utf-8 -*

from mamba import describe, context

from expects import *
from expects.testing import failure


with describe('be_none'):
    def it_should_pass_if_object_is_none():
        expect(None).to(be_none)

    def it_should_fail_if_object_is_not_none():
        with failure('Expected True to be none'):
            expect(True).to(be_none)

    with context('#negated'):
        def it_should_pass_if_object_is_not_none():
            expect('foo').not_to(be_none)

        def it_should_fail_if_object_is_none():
            with failure('Expected None not to be none'):
                expect(None).not_to(be_none)