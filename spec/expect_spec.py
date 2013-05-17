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
                with failure('Expected 1 to equal 2'):
                    expect(1).to.equal(2)

        with describe('be'):
            def it_should_pass_if_actual_is_expected():
                value = 1
                expect(value).to.be(value)

            def it_should_fail_if_actual_is_not_expected():
                with failure('Expected 1 to be 2'):
                    expect(1).to.be(2)

            with describe('true'):
                def it_should_pass_if_actual_is_true():
                    expect(True).to.be.true

                def it_should_fail_if_actual_is_false():
                    with failure('Expected False to be True'):
                        expect(False).to.be.true

            with describe('false'):
                def it_should_pass_if_actual_is_false():
                    expect(False).to.be.false

                def it_should_fail_if_actual_is_true():
                    with failure('Expected True to be False'):
                        expect(True).to.be.false
