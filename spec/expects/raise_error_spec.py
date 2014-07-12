# -*- coding: utf-8 -*

from mamba import describe, context, before

from expects import expect
from expects.testing import failure

NON_STRING_VALUE = 1
STRING_VALUE = 'a string'
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

        with failure(''):
            expect(callback).to(raise_error(AttributeError))

    def it_should_fail_if_callable_does_not_raise_exception():
        with failure(''):
            expect(lambda: None).to(raise_error(AttributeError))

    def it_should_pass_if_callable_raises_with_message():
        def callback():
            raise AttributeError(_.message)

        expect(callback).to(raise_error(AttributeError, _.message))

    def it_should_pass_if_callable_raises_and_message_matches_pattern():
        def callback():
            raise AttributeError(_.message)

        expect(callback).to(raise_error(AttributeError, r'\w+ error'))

    def it_should_pass_if_callable_raises_with_non_string_value():
        def callback():
            raise AttributeError(NON_STRING_VALUE)

        expect(callback).to(raise_error(AttributeError, NON_STRING_VALUE))

    def it_should_pass_if_callable_raises_and_message_matches_unicode_pattern():
        # https://github.com/jaimegildesagredo/expects/issues/17

        def callback():
            raise AttributeError(UNICODE_VALUE)

        expect(callback).to(raise_error(AttributeError, UNICODE_PATTERN))

    def it_should_fail_if_callable_raises_with_different_message():
        def callback():
            raise AttributeError('bar')

        with failure(''):
            expect(callback).to(raise_error(AttributeError, 'foo'))

    def it_should_fail_if_callable_raises_but_message_does_not_match_pattern():
        def callback():
            raise AttributeError(_.message)

        with failure(''):
            expect(callback).to(raise_error(AttributeError, r'\W+ error'))

    def it_should_fail_if_callable_does_not_raise_with_none():
        def callback():
            raise AttributeError(_.message)

        with failure(''):

            expect(callback).to(raise_error(AttributeError, None))

    def it_should_fail_if_callable_does_not_raise_with_non_string_value():
        def callback():
            raise AttributeError(STRING_VALUE)

        with failure(''):
            expect(callback).to(raise_error(AttributeError, NON_STRING_VALUE))

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

            with failure(''):
                expect(callback).not_to(raise_error(AttributeError))

        def it_should_fail_if_callable_raises_expected_exception_with_message():
            def callback():
                raise AttributeError(_.message)

            with failure(''):
                expect(callback).not_to(raise_error(AttributeError, _.message))

    @before.each
    def fixtures():
        _.message = 'Foo error'
