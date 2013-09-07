# -*- coding: utf-8 -*

from mamba import describe, context

from spec.helpers import failure

from expects import expect


with describe('length'):
    def it_should_pass_if_actual_has_the_expected_length():
        expect('foo').to.have.length(3)

    def it_should_fail_if_actual_does_not_have_the_expected_length():
        actual = 'foo'

        with failure(actual, 'to have length 2 but was 3'):
            expect(actual).to.have.length(2)

    def it_should_pass_if_actual_iterable_has_the_expected_length():
        expect(iter('foo')).to.have.length(3)

    def it_should_fail_if_actual_iterable_does_not_have_the_expected_length():
        actual = iter('foo')

        with failure(actual, 'to have length 2 but was 3'):
            expect(actual).to.have.length(2)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_the_expected_length():
            expect('foo').not_to.have.length(2)

        def it_should_fail_if_actual_has_the_expected_length():
            actual = 'foo'

            with failure(actual, 'not to have length 3 but was 3'):
                expect(actual).not_to.have.length(3)
