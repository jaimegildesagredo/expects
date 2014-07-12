# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('empty'):
    def it_should_pass_if_string_empty():
        expect('').to.be(empty)

    def it_should_pass_if_iterable_is_empty():
        expect(iter('')).to.be(empty)

    def it_should_fail_if_string_is_not_empty():
        with failure(''):
            expect('foo').to.be(empty)

    def it_should_fail_if_actual_is_a_non_empty_iterable():
        with failure(''):
            expect(iter('foo')).to.be(empty)

    with context('#negated'):
        def it_should_pass_if_actual_is_not_empty():
            expect('foo').not_to.be(empty)

        def it_should_fail_if_actual_is_empty():
            with failure(''):
                expect('').not_to.be(empty)
