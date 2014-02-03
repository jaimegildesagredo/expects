# -*- coding: utf-8 -*-

from mamba import describe, before
from expects import expect

from spec.helpers import failure


with describe('helpers') as _:
    with describe('failure'):
        def it_should_have_failure_message():
            message = failure(_.actual, _.message).message

            expect(message).to.equal('Expected {} {}'.format(repr(_.actual), _.message))

        def it_should_pass_if_assertion_error_raised_with_message():
            def callback():
                fail = failure(_.actual, _.message)

                with fail:
                    raise AssertionError(fail.message)

            expect(callback).not_to.raise_error(AssertionError)

        def it_should_pass_if_assertion_error_raised_and_matchs_pattern():
            fail = failure(_.actual, _.pattern)

            with fail:
                raise AssertionError(failure(_.actual, _.message).message)

        def it_should_fail_if_assertion_error_not_raised():
            def callback():
                with failure(_.actual, _.message):
                    pass

            expect(callback).to.raise_error(AssertionError)

        def it_should_fail_if_assertion_error_raised_without_message():
            def callback():
                with failure(_.actual, _.message):
                    raise AssertionError('foo')

            expect(callback).to.raise_error(AssertionError)

        @before.each
        def fixtures():
            _.actual = 'foo'
            _.message = "to be 'bar'"
            _.pattern = "to be '\w+'"
