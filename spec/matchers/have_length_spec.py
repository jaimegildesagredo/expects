# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('have_length'):
    def it_should_pass_if_string_has_the_expected_length():
        expect('foo').to(have_length(3))

    def it_should_fail_if_string_does_not_have_the_expected_length():
        with failure("Expected 'foo' to have length 2"):
            expect('foo').to(have_length(2))

    def it_should_pass_if_iterable_has_the_expected_length():
        expect(iter('foo')).to(have_length(3))

    def it_should_fail_if_iterable_does_not_have_the_expected_length():
        with failure('to have length 2'):
            expect(iter('foo')).to(have_length(2))

    with context('#negated'):
        def it_should_pass_if_string_does_not_have_the_expected_length():
            expect('foo').not_to(have_length(2))

        def it_should_fail_if_string_has_the_expected_length():
            with failure("Expected 'foo' not to have length 3"):
                expect('foo').not_to(have_length(3))
