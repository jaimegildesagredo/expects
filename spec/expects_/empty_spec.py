# -*- coding: utf-8 -*

from mamba import describe, context

from ..helpers import failure

from expects import expect


with describe('empty'):
    def it_should_pass_if_actual_is_empty():
        expect('').to.be.empty

    def it_should_pass_if_actual_is_an_empty_iterable():
        expect(iter('')).to.be.empty

    def it_should_fail_if_actual_is_not_empty():
        actual = 'foo'

        with failure(actual, 'to be empty'):
            expect(actual).to.be.empty

    def it_should_fail_if_actual_is_a_non_empty_iterable():
        actual = iter('foo')

        with failure(actual, 'to be empty'):
            expect(actual).to.be.empty

    with context('#negated'):
        def it_should_pass_if_actual_is_not_empty():
            expect('foo').not_to.be.empty

        def it_should_fail_if_actual_is_empty():
            actual = ''

            with failure(actual, 'not to be empty'):
                expect(actual).not_to.be.empty
