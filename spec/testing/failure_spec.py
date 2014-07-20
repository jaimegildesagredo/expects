# -*- coding: utf-8 -*-

from mamba import describe, before

from expects import expect
from expects.matchers import *
from expects.testing import failure


with describe('failure') as _:
    def it_should_pass_if_assertion_error_raised_and_message_matches():
        def callback():
            with failure(_.message):
                raise AssertionError("Expected 'foo' {}".format(_.message))

        expect(callback).not_to(raise_error(AssertionError))

    def it_should_pass_if_assertion_error_raised_and_pattern_matches():
        def callback():
            with failure(_.pattern):
                raise AssertionError("Expected 'foo' {}".format(_.message))

        expect(callback).not_to(raise_error(AssertionError))

    def it_should_fail_if_assertion_error_not_raised():
        def callback():
            with failure(_.message):
                pass

        expect(callback).to(raise_error(AssertionError))

    def it_should_fail_if_assertion_error_raised_and_message_does_not_match():
        def callback():
            with failure(_.message):
                raise AssertionError('foo')

        expect(callback).to(raise_error(AssertionError))

    def it_should_fail_if_another_exception_raised():
        def callback():
            with failure(_.message):
                raise KeyError()

        expect(callback).to(raise_error(AssertionError))

    @before.each
    def fixtures():
        _.message = "to be 'bar'"
        _.pattern = "to be '\w+'"
