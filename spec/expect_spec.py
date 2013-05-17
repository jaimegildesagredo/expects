# -*- coding: utf-8 -*

from mamba import describe
from spec.helpers import failure

from expects import expect

with describe(expect) as _:
    with describe('to'):
        with describe('equal'):
            def it_should_pass_if_actual_equals_expected():
                expect(1).to.equal(1)

            def it_should_fail_if_actual_does_not_equal_expected():
                with failure('Expected 1 to be 2'):
                    expect(1).to.equal(2)

            def it_should_show_quoted_strings_on_failure():
                with failure("Expected 'foo' to be 'bar'"):
                    expect('foo').to.equal('bar')
