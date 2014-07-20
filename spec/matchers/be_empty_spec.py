# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('be_empty'):
    def it_should_pass_if_string_empty():
        expect('').to(be_empty)

    def it_should_pass_if_iterable_is_empty():
        expect(iter('')).to(be_empty)

    def it_should_fail_if_string_is_not_empty():
        with failure("Expected 'foo' to be empty"):
            expect('foo').to(be_empty)

    def it_should_fail_if_actual_is_a_non_empty_iterable():
        with failure('to be empty'):
            expect(iter('foo')).to(be_empty)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_empty():
            expect('foo').not_to(be_empty)

        def it_should_fail_if_actual_is_empty():
            with failure("Expected '' not to be empty"):
                expect('').not_to(be_empty)
