# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.matchers import *
from expects.testing import failure

UNICODE_VALUE = u'an unicode value'
UNICODE_PATTERN = u'unicode'


with describe('raise_error') as _:
    def it_should_pass_if_callable_raises_expected_exception():
        def callback():
            raise AttributeError()

        expect(callback).to(raise_error(AttributeError))

    def it_should_fail_if_callable_does_not_raise_expected_exception():
        def callback():
            raise KeyError()

        with failure('to raise AttributeError but KeyError raised'):
            expect(callback).to(raise_error(AttributeError))

    def it_should_fail_if_callable_does_not_raise_exception():
        with failure('to raise AttributeError but not raised'):
            expect(lambda: None).to(raise_error(AttributeError))

    def it_should_pass_if_callable_raises_with_message():
        def callback():
            raise AttributeError(_.message)

        expect(callback).to(raise_error(AttributeError, _.message))

    def it_should_pass_if_callable_raises_with_non_string_value():
        def callback():
            raise AttributeError(1)

        expect(callback).to(raise_error(AttributeError, 1))

    def it_should_fail_if_callable_raises_with_different_message():
        def callback():
            raise AttributeError('bar')

        with failure("to raise AttributeError with 'foo' but was 'bar'"):
            expect(callback).to(raise_error(AttributeError, 'foo'))

    def it_should_fail_if_callable_does_not_raise_with_none():
        def callback():
            raise AttributeError('foo')

        with failure("to raise AttributeError with None but was 'foo'"):
            expect(callback).to(raise_error(AttributeError, None))

    def it_should_fail_if_callable_does_not_raise_with_non_string_value():
        def callback():
            raise AttributeError('foo')

        with failure("to raise AttributeError with 1 but was 'foo'"):
            expect(callback).to(raise_error(AttributeError, 1))

    with context('#negated'):
        def it_should_pass_if_callable_does_not_raise_expected_exception():
            def callback():
                raise AttributeError()

            expect(callback).not_to(raise_error(KeyError))

        def it_should_pass_if_callable_does_not_raise_exception():
            expect(lambda: None).not_to(raise_error(AttributeError))

        def it_should_pass_if_callable_raises_expected_exception_with_different_message():
            def callback():
                raise AttributeError('bar')

            expect(callback).not_to(raise_error(AttributeError, 'foo'))

        def it_should_fail_if_callable_raises_expected_exception():
            def callback():
                raise AttributeError()

            with failure('not to raise AttributeError but AttributeError raised'):
                expect(callback).not_to(raise_error(AttributeError))

        def it_should_fail_if_callable_raises_expected_exception_with_message():
            def callback():
                raise AttributeError('foo')

            with failure("not to raise AttributeError with 'foo' "
                         "but AttributeError raised with 'foo'"):

                expect(callback).not_to(raise_error(AttributeError, 'foo'))

    with context('#combined'):
        def it_should_pass_if_callable_raises_exception_and_message_matches():
            def callback():
                raise AttributeError(_.message)

            expect(callback).to(raise_error(AttributeError, match(r'Foo \w+')))

        def it_should_fail_if_callable_raises_but_message_does_not_match():
            def callback():
                raise AttributeError('foo')

            with failure("to raise AttributeError with match '\\\\d+' but was 'foo'"):
                expect(callback).to(raise_error(AttributeError, match(r'\d+')))

    @before.each
    def fixtures():
        _.message = 'Foo error'
